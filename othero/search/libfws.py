# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import enum

from othero.core import libdisk, libtypes
from othero.rule import libforward
from othero.search import utils

def get_available_positions(sog, disk):
    """
    Return a list of positions in <sog> where putting <disk> is allowed.

    Args:
        sog othero.core.libsog.SOG:
            Sog to be searched in. 
        
        disk othero.core.libtypes.Disk:
            Disk to be put.
    
    Returns:
        [(int, int)]:
            List of positions in <sog> where putting <disk> is allowed.
    """
    sos = libtypes.Disk.toSOS(disk)

    blank_poss = sog.getPositionsInSos(libtypes.SOS.BLANK)
    return [pos for pos in blank_poss \
                if libforward.is_sos_change_valid(sog, pos, sos)]

def calc_all_next_sogs(sog, disk):
    """
    Restore sos at the <pos> to <sos> and calculate the resulting
    possible sogs according to the osero rule.

    Args: 
        sog othero.core.libsog.SOG:

        disk othero.core.libtypes.Disk:
            A disk to be put.

    Returns:
        [othero.core.libsog.SOG]:
            A list of possible sogs in the next turn. If there is no
            position at which <disk> can be put, the list is empty.
    """
    sos = libtypes.Disk.toSOS(disk)
    return [libforward.calc_sog_after_sos_changed(sog, pos, sos)
                for pos in get_available_positions(sog, disk)]

class FwsNode:
    class ReservedKeys(enum.Enum):
        IS_DTW = "isDtw"

    @classmethod
    def create(cls, tree, prev_node, cur_sog, prev_disk):
        """
        Create a new FwsNode instance and return it.

        Args:
            tree othero.search.libfws.FwsTree:
                The tree which a new node belongs to.

            prev_node othero.search.libfws.FwsNode:
                The parent node of a new node.
            
            cur_sog othero.core.libsog.SOG:
                The sog which a new node contains.

        Returns:
            othero.search.libfws.FwsNode:
        """
        node = cls()
        node.setParams(tree, prev_node, cur_sog, prev_disk)
        node.initialize()
        return node

    @classmethod
    def delete(cls, tree, node):
        """
        This method is reserved to be used in derived classes.

        This is called when a node is no longer used and can be released.

        Args:
            tree othero.search.libfws.FwsTree:
                The tree which the <node> belongs to.
            
            node othero.search.libfws.FwsNode:
                The node to be deleted.
        """
        pass

    def setParams(self, tree, prev_node, cur_sog, prev_disk):
        """
        Initialize instance variables with given parameters.

        Args:
            tree othero.search.libfws.FwsTree:
            
            prev_node othero.search.libfws.FwsNode:

            cur_sog othero.core.libsog.SOG:

            prev_disk othero.core.libtypes.Disk:
        """
        self.cur_sog = cur_sog
        self.next_nodes = None 
        self.prev_node = prev_node
        self.next_disk = None
        self.prev_disk = prev_disk
        self.isLeaf = None
        self.__next_sogs = None
        self.tree = tree
        self.__mark = {}

    def initialize(self):
        """
        Calculate the inner state of the node.
        """
        self.__search_nexts()

    def expand(self):
        """
        Create nodes for all the possible sogs in the next turn. Once a
        node gets no longer to be used, it should be shrinked to reduce the
        memory usage.

        The new nodes are stores in <self>.<next_nodes>.
        """
        if self.next_nodes == None:
            if self.__next_sogs == None:
                self.__search_nexts()
            self.next_nodes = [
                self.create(self.tree, self, sog, self.next_disk)
                for sog in self.__next_sogs
            ]

    def shrink(self):
        """
        Release the nodes in <self>.<next_nodes>. This method should be called
        after expand is called.
        """
        for node in self.next_nodes:
            self.delete(self.tree, node)
        self.next_nodes = None
        self.__next_sogs = None

    def addMark(self, key, value):
        """
        Add a key value pair to the node. The added value can be retrieved by
        getMark with the key.

        Args:
            key string:
            
            value *:
        """
        self.__mark[key] = value

    def getMark(self, key):
        """
        Get the value which are related to <key>.

        Args:
            key string:
        
        Returns:
            *:
                The value related to <key>.
        """
        if key not in self.__mark.keys():
            return None
        return self.__mark[key]

    def delMark(self, key):
        """
        Delete the key value pair which was added to the node.

        Args:
            key string:
        """
        if key in self.__mark.keys():
            del self.__mark[key]

    def __search_nexts(self):
        next_disk = libdisk.next_disk(self.prev_disk)
        for _ in range(len(libtypes.Disk)):
            next_sogs = calc_all_next_sogs(self.cur_sog, next_disk)
            if len(next_sogs) == 0:
                next_disk = libdisk.next_disk(next_disk)
                continue
            break
        else:
            self.isLeaf = True
            self.next_disk = None
            self.__next_sogs = []
            return
        
        self.isLeaf = False
        self.next_disk = next_disk
        self.__next_sogs = next_sogs

class FwsTree:
    def __init__(self, sog, first_disk=libtypes.Disk.DARK):
        self.root = FwsNode.create(self, None, sog, libdisk.prev_disk(first_disk))

# stateless crawler
class FwsCrawler:
    def __init__(self, my_disk, start_node):
        self.__my_disk = my_disk
        self.__cur_node = start_node

    def duplicate(self):
        """
        Duplicate oneself and return the copy.

        This method is intended to be used when the search need to procede
        in a concurrent manner.
        
        Returns:
            othero.search.libfws.FwsCrawler:
        """
        return type(self)(self.__my_disk, self.__cur_node)

    # nid: node number
    def advance(self, nid):
        """
        Advance to one of the next nodes along with the search tree.
        As more than one nodes exist in the next turn, which node the
        crawler goes to is specified by <nid>.

        Args:
            nid int:
                The index pointing into <self>.<__cur_node>.<next_nodes>.
        """
        self.__cur_node = self.__cur_node.next_nodes[nid]

    def retreat(self):
        """
        Retreat to the previous node.
        """
        self.__cur_node = self.__cur_node.prev_node

    def expandNode(self):
        """
        Make the current node expand for further search.
        """
        self.__cur_node.expand()
        return len(self.__cur_node.next_nodes)

    def shrinkNode(self):
        """
        Make the current node shrink for memory optimization.
        """
        self.__cur_node.shrink()

    def storeMark(self, key, value):
        """
        Store the key value pair in the current node.

        Args:
            key string:

            value *:
        """
        self.__cur_node.addMark(key, value)

    def loadMark(self, key):
        """
        Load the value related to <key> from the current node.

        Args:
            key string:

        Returns:
            value *:
        """
        return self.__cur_node.getMark(key)

    def hasReachedLeaf(self):
        """
        Return if the current node is a leaf, that is, if the game is over.
        """
        return self.__cur_node.isLeaf

    # DTW := destined to winning
    def calcIsDtw(self):
        """
        Calculate if the player with <self>.<__my_disk> is destined to win.

        Returns:
            bool:
        """
        cache = self.loadMark(FwsNode.ReservedKeys.IS_DTW)
        if cache is not None:
            return cache

        def getIsDTWFromNode(node):
            return node.getMark(FwsNode.ReservedKeys.IS_DTW)

        if self.__cur_node.isLeaf:
            if utils.get_winner_disk(self.__cur_node.cur_sog) == self.__my_disk:
                return True
            else:
                return False

        dtws = [getIsDTWFromNode(node)
            for node in self.__cur_node.next_nodes]
        if self.__cur_node.next_disk == self.__my_disk:
            if set(dtws) == {None}:
                return None
            return any(dtws)
        else:
            if None in dtws:
                return None
            return all(dtws)

    def storeIsDtw(self):
        """
        Store the result of calcIsDtw in the current node.
        """
        self.storeMark(FwsNode.ReservedKeys.IS_DTW, self.calcIsDtw())

    def loadIsDtw(self):
        """
        Load the result of calcIsDtw in the current node.

        Returns:
            bool:
                isDtw of the current node.
        """
        return self.loadMark(FwsNode.ReservedKeys.IS_DTW)

    def run(self):
        """
        Execute depth first search for the procedure by which the player with <self>.<__mydisk>
        never fails to win. The search is conducted by recursive calls of this function.
        """
        if self.hasReachedLeaf():
            self.storeIsDtw()
            return

        nnode = self.expandNode()
        for i in range(nnode):
            self.advance(i)
            self.run()
            self.storeIsDtw()
            self.retreat()
        self.storeIsDtw()
        self.shrinkNode()

def calc_is_dtw(sog, my_disk, first_disk=libtypes.Disk.DARK):
    """
    Return if the player with <my_disk> never fails to win.

    Args:
        sog othero.core.libsog.SOG:
            The sog with which the search begins.

        my_disk othero.core.libtypes.Disk:

        first_disk othero.core.libtypes.Disk:
            The disk which is put at first.
    
    Returns:
        bool:
    """
    tree = FwsTree(sog, first_disk)
    crawler = FwsCrawler(my_disk, tree.root)
    crawler.run()
    return crawler.calcIsDtw()

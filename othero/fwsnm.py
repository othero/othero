# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes, libsog, libdisk
from othero.search import libfws

class FwsNodeManager:
    def __init__(self, cls, size, ninc=10):
        self.__cls = cls
        self.__stack = self.__newNodes(size)
        self.__size = size
        self.__ninc = ninc
        self.__sp = 0
        self.__reserved = []

    def alloc(self):
        """
        Allocate a node and return it.
        
        Returns:
            othero.search.libfws.FwsNode:
        
        """
        if self.__sp >= self.__size:
            self.__stack = self.__stack \
                + self.__newNodes(self.__ninc)
            self.__size = self.__size + self.__ninc
        while True:
            node = self.__pop()
            if id(node) not in self.__reserved:
                break
        self.__reserved.append(id(node))
        return node

    def free(self, node):
        """
        Free the allocated <node> to be used later.

        Args:
            node othero.search.libfws.FwsNode:
                The node to be freed.
        """
        if id(node) in self.__reserved:
            self.__push(node)
            self.__reserved.remove(id(node))

    def __pop(self):
        node = self.__stack[self.__sp]
        self.__sp += 1
        return node

    def __push(self, node):
        self.__sp -= 1
        self.__stack[self.__sp] = node

    def __newNodes(self, nnode):
        return [
            self.__cls()
            for _ in range(nnode)
        ]

class FwsNodeWithManager(libfws.FwsNode):
    @classmethod
    def create(cls, tree, prev_node, cur_sog, prev_disk):
        """
        Create a new FwsNodeWithManager instance and return it. The instance is
        allocated by <tree>.<fwsnm> manager.

        Args:
            tree othero.fws.FwsTreeWithManager:
                The tree which a new node belongs to.

            prev_node othero.search.libfws.FwsNode:
                The parent node of a new node.
            
            cur_sog othero.core.libsog.SOG:
                The sog which a new node contains.

        Returns:
            othero.fws.FwsNodeWithManager:
        """
        node = tree.fwsnm.alloc()
        node.setParams(tree, prev_node, cur_sog, prev_disk)
        node.initialize()
        return node

    @classmethod
    def delete(cls, tree, node):
        """
        Free an allocated node. The node need to have been allocated by
        <tree>.<fwsnm>.

        Args:
            tree othero.fws.FwsTreeWithManager:
                The tree which the <node> belongs to.
            
            node othero.fws.FwsNodeWithManager:
                The node to be freed.
        """
        tree.fwsnm.free(node)

class FwsTreeWithManager(libfws.FwsTree):
    def __init__(self, sog, stack_size, stack_ninc=10, first_disk=libtypes.Disk.DARK):
        self.fwsnm = FwsNodeManager(FwsNodeWithManager, stack_size, stack_ninc)
        self.root = FwsNodeWithManager.create(self, None, sog, libdisk.prev_disk(first_disk))

def calc_is_dtw_with_manager(sog, my_disk, first_disk=libtypes.Disk.DARK):
    """
    Return if the player with <my_disk> never fails to win. The search is
    conducted with a help of FwsNodeManager.

    Args:
        sog othero.core.libsog.SOG:
            The sog with which the search begins.

        my_disk othero.core.libtypes.Disk:
            
        first_disk othero.core.libtypes.Disk:
            The disk which is put at first.
    
    Returns:
        bool:
    """
    tree = FwsTreeWithManager(sog, 100, 10, first_disk)
    crawler = libfws.FwsCrawler(my_disk, tree.root)
    crawler.run()
    return crawler.calcIsDtw()

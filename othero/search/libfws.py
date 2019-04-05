# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import enum

from othero.core import libboard, libdisk, libtypes
from othero.rule import libforward
from othero.search import utils

def get_available_positions(sog, disk):
    """
    Return a list of positions in <sog> where putting <disk> is allowed.

    Args:
        sog [[othero.core.libtypes.SOS]]:
            Sog to be searched in. 
        
        disk othero.core.libtypes.Disk:
            Disk to be put.
    
    Returns:
        [(int, int)]:
            List of positions in <sog> where putting <disk> is allowed.
    """
    sos = libtypes.Disk.toSOS(disk)

    blank_poss = libboard.get_positions_in_sos(sog, libtypes.SOS.BLANK)
    return [pos for pos in blank_poss \
                if libforward.is_sos_change_valid(sog, pos, sos)]

def calc_all_next_sogs(sog, disk):
    """
    Restore sos at the <pos> to <sos> and calculate the resulting
    possible sogs according to the osero rule.

    Args: 
        sog [[othero.core.libtypes.SOS]]:

        disk othero.core.libtypes.Disk:
            A disk to be put.

    Returns:
        [[[othero.core.libtypes.SOS]]]:
            A list of possible sogs in the next turn. If there is no
            position at which <disk> can be put, the list is empty.
    """
    sos = libtypes.Disk.toSOS(disk)
    return [libforward.calc_sog_after_sos_changed(sog, pos, sos)
                for pos in get_available_positions(sog, disk)]

class FwsNode:
    class ReservedKeys(enum.Enum):
        IS_DTW = "isDtw"

    @staticmethod
    def create(tree, prev_node, cur_sog, prev_disk):
        node = FwsNode()
        node.setParams(tree, prev_node, cur_sog, prev_disk)
        node.initialize()
        return node

    @staticmethod
    def delete(tree, node):
        pass

    def setParams(self, tree, prev_node, cur_sog, prev_disk):
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
        self.__search_nexts()

    def expand(self):
        if self.next_nodes == None:
            if self.__next_sogs == None:
                self.__search_nexts()
            self.next_nodes = [
                self.create(self.tree, self, sog, self.next_disk)
                for sog in self.__next_sogs
            ]

    def shrink(self):
        for node in self.next_nodes:
            self.delete(self.tree, node)
        self.next_nodes = None
        self.__next_sogs = None

    def addMark(self, key, value):
        self.__mark[key] = value

    def getMark(self, key):
        if key not in self.__mark.keys():
            return None
        return self.__mark[key]

    def delMark(self, key):
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

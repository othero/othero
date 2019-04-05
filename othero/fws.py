# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libdisk, libsog, libtypes
from othero.search import libfws

class FwsNodeManager:
    def __init__(self, size, ninc=10):
        self.__stack = self.__newNodes(size)
        self.__size = size
        self.__ninc = ninc
        self.__sp = 0
        self.__reserved = []

    def alloc(self):
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
            FwsNodeWithManager()
            for _ in range(nnode)
        ]

class FwsNodeWithManager(libfws.FwsNode):
    @staticmethod
    def create(tree, prev_node, cur_sog, prev_disk):
        node = tree.fwsnm.alloc()
        node.setParams(tree, prev_node, cur_sog, prev_disk)
        node.initialize()
        return node

    @staticmethod
    def delete(tree, node):
        tree.fwsnm.free(node)

class FwsTreeWithManager(libfws.FwsTree):
    def __init__(self, sog, stack_size, stack_ninc=10, first_disk=libtypes.Disk.DARK):
        self.fwsnm = FwsNodeManager(stack_size, stack_ninc)
        self.root = FwsNodeWithManager.create(self, None, sog, libdisk.prev_disk(first_disk))

# depth-first
def run(crawler):
    if crawler.hasReachedLeaf():
        crawler.storeIsDtw()
        return

    nnode = crawler.expandNode()
    for i in range(nnode):
        crawler.advance(i)
        run(crawler)
        crawler.storeIsDtw()
        crawler.retreat()
    crawler.storeIsDtw()
    crawler.shrinkNode()

def calc_is_dtw(sog, my_disk, first_disk=libtypes.Disk.DARK):
    tree = libfws.FwsTree(sog, first_disk)
    crawler = libfws.FwsCrawler(my_disk, tree.root)
    run(crawler)
    return crawler.calcIsDtw()

def calc_is_dtw_with_manager(sog, my_disk, first_disk=libtypes.Disk.DARK):
    tree = FwsTreeWithManager(sog, 100, 10, first_disk)
    crawler = libfws.FwsCrawler(my_disk, tree.root)
    run(crawler)
    return crawler.calcIsDtw()

if __name__ == "__main__":
    print(calc_is_dtw(libsog.create_sog(), libtypes.Disk.LIGHT))

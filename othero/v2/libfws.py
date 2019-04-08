# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import enum

from othero.core import libtypes, libdisk
from othero.search import libfws

class FwsNode(libfws.FwsNode):
    class ReservedKeys(enum.Enum):
        IS_DTW = "isDtw"
        EVAL = "eval"

    def evaluate(self):
        poss = self.cur_sog.getAllPositions()

        edark, elight = 0, 0
        for pos in poss:
            sos = self.cur_sog.getSos(pos)
            esp = self.cur_sog.getEsp(pos)
            if sos == libtypes.SOS.DARK:
                edark += esp
            elif sos == libtypes.SOS.LIGHT:
                elight += esp
        return edark, elight

class FwsTree:
    def __init__(self, sog, first_disk=libtypes.Disk.DARK):
        self.root = FwsNode.create(self, None, sog, libdisk.prev_disk(first_disk))

class FwsCrawler(libfws.FwsCrawler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    def evalNode(self, node=None):
        if node is None:
            node = self.__cur_node
        edark, elight = node.evaluate()
        if self.__my_disk == libtypes.Disk.DARK:
            return edark - elight
        elif self.__my_disk == libtypes.Disk.LIGHT:
            return elight - edark

    def storeEval(self):
        self.storeMark(FwsNode.ReservedKeys.EVAL, self.evalNode())

    def loadEval(self):
        return self.loadMark(FwsNode.ReservedKeys.EVAL)

    def run(self):
        if self.hasReachedLeaf():
            self.storeIsDtw()
            self.counter += 1
            return

        nnode = self.expandNode()

        if self.__my_disk == self.__cur_node.next_disk:
            self.__cur_node.next_nodes.sort(
                reverse=True,
                key=lambda node: self.evalNode(node)
            )
        elif self.__my_disk != self.__cur_node.next_disk:
            self.__cur_node.next_nodes.sort(
                reverse=False,
                key=lambda node: self.evalNode(node)
            )

        for i in range(nnode):
            self.advance(i)
            self.run()

            isDtw = self.loadIsDtw()
            wasMyTurn = self.__my_disk == self.__cur_node.prev_disk
            hasDetermined = (isDtw and wasMyTurn) \
                or ((not isDtw) and (not wasMyTurn))

            self.retreat()
            if hasDetermined:
                break
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
    print(f"{crawler.counter} final sogs were visited in total.")
    return crawler.calcIsDtw()

# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero import fws
from othero.core import libtypes
from othero.search import libfws

class TestFws(unittest.TestCase):
    def test_calc_is_dtw_with_manager(self):
        sog = [
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT]
        ]
        self.assertFalse(fws.calc_is_dtw_with_manager(sog, libtypes.Disk.DARK, libtypes.Disk.DARK))

class TestFwsFwsNodeWithManager(unittest.TestCase):
    __SOG = [
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK ],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
    ]

    def test_create(self):
        tree = fws.FwsTreeWithManager(self.__SOG, 100)
        node = libfws.FwsNode.create(tree, tree.root, self.__SOG, libtypes.Disk.LIGHT)
        self.assertEqual(node.cur_sog, self.__SOG)
        self.assertEqual(node.prev_node, tree.root)
        self.assertEqual(node.prev_disk, libtypes.Disk.LIGHT)
        self.assertEqual(node.tree, tree)
        self.assertEqual(node.next_disk, libtypes.Disk.DARK)
        self.assertFalse(node.isLeaf)

        self.assertIsNone(node.next_nodes)

    def test_delete(self):
        pass

    def test_expand(self):
        def is_equal(x, y):
            return all([a in y for a in x]) \
                    and all([a in x for a in y])

        tree = fws.FwsTreeWithManager(self.__SOG, 100)
        node = libfws.FwsNode.create(tree, tree.root, self.__SOG, libtypes.Disk.LIGHT)
        node.expand()
        self.assertIsNotNone(node.next_nodes)
        self.assertTrue(is_equal(
            list(map(lambda nd: nd.cur_sog, node.next_nodes)),
            libfws.calc_all_next_sogs(node.cur_sog, node.next_disk)
        ))

    def test_shrink(self):
        tree = fws.FwsTreeWithManager(self.__SOG, 100)
        node = libfws.FwsNode.create(tree, tree.root, self.__SOG, libtypes.Disk.LIGHT)
        node.expand()
        node.shrink()
        self.assertIsNone(node.next_nodes)
        self.assertEqual(node.next_disk, libtypes.Disk.DARK) 
        self.assertFalse(node.isLeaf)

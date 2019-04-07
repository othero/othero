# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libtypes
from othero.search import libfws
from test import testutils

class TestSearchFws(unittest.TestCase):
    __SOG = testutils.sosss_to_sog([
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK ],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
    ])

    def test_get_available_positions(self):
        self.assertEqual(
            libfws.get_available_positions(self.__SOG, libtypes.Disk.DARK),
            [(0, 2), (1, 2), (2, 2)]
        )

    def test_calc_all_next_sogs1(self):
        def is_equal(x, y):
            return all([a in y for a in x]) \
                    and all([a in x for a in y])

        expect = [
            testutils.sosss_to_sog([
                [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK ],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
            ]),
            testutils.sosss_to_sog([
                [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK ],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK] 
            ]),
            testutils.sosss_to_sog([
                [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK ],
                [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK],
                [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
            ]),
        ]

        self.assertTrue(is_equal(
            libfws.calc_all_next_sogs(self.__SOG, libtypes.Disk.DARK),
            expect
        ))

    def test_calc_all_next_sogs2(self):
        self.assertEqual(
            libfws.calc_all_next_sogs(self.__SOG, libtypes.Disk.LIGHT),
            [] 
        )

    def test_calc_is_dtw1(self):
        sog = testutils.sosss_to_sog([
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT]
        ])
        self.assertFalse(libfws.calc_is_dtw(sog, libtypes.Disk.DARK, libtypes.Disk.DARK))

    def test_calc_is_dtw2(self):
        sog = testutils.sosss_to_sog([
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.BLANK]
        ])
        self.assertTrue(libfws.calc_is_dtw(sog, libtypes.Disk.DARK, libtypes.Disk.DARK))

    def test_calc_is_dtw3(self):
        sog = testutils.sosss_to_sog([
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.BLANK]
        ])
        self.assertFalse(libfws.calc_is_dtw(sog, libtypes.Disk.LIGHT, libtypes.Disk.DARK))


class TestSearchFwsFwsNode(unittest.TestCase):
    __SOG = testutils.sosss_to_sog([
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK ],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
    ])

    __TREE = libfws.FwsTree(__SOG)

    def test_create(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        self.assertEqual(node.cur_sog, self.__SOG)
        self.assertEqual(node.prev_node, self.__TREE.root)
        self.assertEqual(node.prev_disk, libtypes.Disk.LIGHT)
        self.assertEqual(node.tree, self.__TREE)
        self.assertEqual(node.next_disk, libtypes.Disk.DARK)
        self.assertFalse(node.isLeaf)

        self.assertIsNone(node.next_nodes)

    def test_delete(self):
        pass

    def test_setParams(self):
        node = libfws.FwsNode()
        node.setParams(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        self.assertEqual(node.cur_sog, self.__SOG)
        self.assertEqual(node.prev_node, self.__TREE.root)
        self.assertEqual(node.prev_disk, libtypes.Disk.LIGHT)
        self.assertEqual(node.tree, self.__TREE)

        self.assertIsNone(node.next_nodes)
        self.assertIsNone(node.next_disk)
        self.assertIsNone(node.isLeaf)

    def test_initialize(self):
        node = libfws.FwsNode()
        node.setParams(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        node.initialize() 
        self.assertEqual(node.next_disk, libtypes.Disk.DARK)
        self.assertIsNotNone(node.isLeaf)

    def test_expand(self):
        def is_equal(x, y):
            return all([a in y for a in x]) \
                    and all([a in x for a in y])

        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        node.expand()
        self.assertIsNotNone(node.next_nodes)
        self.assertTrue(is_equal(
            list(map(lambda nd: nd.cur_sog, node.next_nodes)),
            libfws.calc_all_next_sogs(node.cur_sog, node.next_disk)
        ))

    def test_shrink(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        node.expand()
        node.shrink()
        self.assertIsNone(node.next_nodes)
        self.assertEqual(node.next_disk, libtypes.Disk.DARK) 
        self.assertFalse(node.isLeaf)

    def test_getMark(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        self.assertIsNone(node.getMark("key"))

    def test_addMark__getMark(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        node.addMark("key", "value")
        self.assertEqual(node.getMark("key"), "value")

    def test_delMark(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        node.addMark("key", "value")
        node.delMark("key")
        self.assertIsNone(node.getMark("key"))

class TestSearchFwsFwsCrawler(unittest.TestCase):
    __SOG = testutils.sosss_to_sog([
            [libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
            [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK],
            [libtypes.SOS.BLANK, libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.BLANK],
            [libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK]
        ])

    __TREE = libfws.FwsTree(__SOG)

    __ROOT = libfws.FwsNode.create(__TREE, __TREE.root, __SOG, libtypes.Disk.LIGHT)

    def test_expandNode(self):
        crawler = libfws.FwsCrawler(libtypes.Disk.DARK, self.__ROOT)
        self.assertGreater(crawler.expandNode(), 0)

    def test_loadMark(self):
        crawler = libfws.FwsCrawler(libtypes.Disk.DARK, self.__ROOT)
        self.assertIsNone(crawler.loadMark("key"))

    def test_storeMark__loadMark(self):
        crawler = libfws.FwsCrawler(libtypes.Disk.DARK, self.__ROOT)
        crawler.storeMark("key", "value")
        self.assertEqual(crawler.loadMark("key"), "value")

    def test_hasReachedLeaf(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        node.isLeaf = True
        crawler = libfws.FwsCrawler(libtypes.Disk.DARK, node)
        self.assertTrue(crawler.hasReachedLeaf)

    def test_calcIsDtw1(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        crawler = libfws.FwsCrawler(libtypes.Disk.DARK, node)
        crawler.expandNode()
        for nd in node.next_nodes:
            nd.addMark(libfws.FwsNode.ReservedKeys.IS_DTW, True) 
        node.next_nodes[0].addMark(libfws.FwsNode.ReservedKeys.IS_DTW, False)
        self.assertTrue(crawler.calcIsDtw())

    def test_calcIsDtw2(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        crawler = libfws.FwsCrawler(libtypes.Disk.LIGHT, node)
        crawler.expandNode()
        for nd in node.next_nodes:
            nd.addMark(libfws.FwsNode.ReservedKeys.IS_DTW, True) 
        node.next_nodes[0].addMark(libfws.FwsNode.ReservedKeys.IS_DTW, False)
        self.assertFalse(crawler.calcIsDtw())

    def test_storeIsDtw__loadIsDtw(self):
        node = libfws.FwsNode.create(self.__TREE, self.__TREE.root, self.__SOG, libtypes.Disk.LIGHT)
        crawler = libfws.FwsCrawler(libtypes.Disk.LIGHT, node)
        crawler.expandNode()
        for nd in node.next_nodes:
            nd.addMark(libfws.FwsNode.ReservedKeys.IS_DTW, True) 
        crawler.storeIsDtw()
        self.assertTrue(crawler.loadIsDtw())

# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest
from othero.core import types
from othero.game import utils

class TestGameUtils(unittest.TestCase):
    __SOG = [ \
        [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
    ]

    def test_calc_sog_after_put_disk(self):
        SOG2 = [ \
            [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
            [types.SOS.DARK , types.SOS.DARK, types.SOS.DARK, types.SOS.BLANK,], \
            [types.SOS.DARK , types.SOS.DARK, types.SOS.BLANK, types.SOS.BLANK,], \
            [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
        ]
        self.assertEqual(
            utils.calc_sog_after_put_disk(self.__SOG, (1, 2), types.Disk.DARK),
            SOG2
        )
    
    def test_is_put_disk_valid1(self):
        self.assertEqual(
            utils.is_put_disk_valid(self.__SOG, (1, 2), types.Disk.DARK),
            True
        )

    def test_is_put_disk_valid2(self):
        self.assertEqual(
            utils.is_put_disk_valid(self.__SOG, (1, 2), types.Disk.LIGHT),
            False
        )

    def test_get_available_positions(self):
        self.assertEqual(
            utils.get_available_positions(self.__SOG, types.Disk.DARK),
            [(1, 2), (2, 2)]
        )

class TestGameUtilsGame(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
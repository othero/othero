# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import board, types

class TestCoreBoard(unittest.TestCase):
    __SOG = [ \
        [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
    ]

    def test_count_soss(self):
        self.assertEqual(
            board.count_soss(self.__SOG),
            (7, 3, 6)
        )
    
    def test_get_positions_in_sos(self):
        self.assertEqual(
            board.get_positions_in_sos(self.__SOG, types.SOS.BLANK),
            [(0, 0), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        )
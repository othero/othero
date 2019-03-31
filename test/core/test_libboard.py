# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libboard, libtypes

class TestCoreBoard(unittest.TestCase):
    __SOG = [ \
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK] \
    ]

    def test_count_soss(self):
        self.assertEqual(
            libboard.count_soss(self.__SOG),
            (7, 3, 6)
        )
    
    def test_get_positions_in_sos(self):
        self.assertEqual(
            libboard.get_positions_in_sos(self.__SOG, libtypes.SOS.BLANK),
            [(0, 0), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        )
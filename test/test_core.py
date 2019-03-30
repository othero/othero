# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero import core

class TestCore(unittest.TestCase):
    __sog = [ \
        [core.SOS.BLANK, core.SOS.DARK , core.SOS.LIGHT, core.SOS.DARK ,], \
        [core.SOS.DARK , core.SOS.LIGHT, core.SOS.BLANK, core.SOS.BLANK,], \
        [core.SOS.DARK , core.SOS.LIGHT, core.SOS.BLANK, core.SOS.BLANK,], \
        [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK] \
    ]

    __sog_str = \
        "0,1,-1,1," + \
        "1,-1,0,0," + \
        "1,-1,0,0," + \
        "1,1,1,0"

    def test_calc_sid1(self):
        self.assertEqual(
            core.calc_sid(TestCore.__sog, (1, 2), core.SOS.DARK, core.Direction.LOW_L),
            1
        )

    def test_calc_sid2(self):
        self.assertEqual(
            core.calc_sid(TestCore.__sog, (1, 2), core.SOS.BLANK, core.Direction.LOW_L),
            0
        )

    def test_calc_all_sids(self):
        expect = {
            core.Direction.UP: 0,
            core.Direction.UP_R: 0,
            core.Direction.RIGHT: 0,
            core.Direction.LOW_R: 0,
            core.Direction.LOW: 0,
            core.Direction.LOW_L: 1,
            core.Direction.LEFT: 1,
            core.Direction.UP_L: 0
        }
        self.assertEqual(
            core.calc_all_sids(TestCore.__sog, (1, 2), core.SOS.DARK),
            expect
        )
    
    def test_advance_pos(self):
        self.assertEqual(
            core.advance_pos((1, 2), core.Direction.LOW_L, 2),
            (3, 0)
        )

    def test_is_in_board1(self):
        self.assertEqual(
            core.is_in_board((1, 2)),
            True
        )

    def test_is_in_board2(self):
        self.assertEqual(
            core.is_in_board((4, 0)),
            False
        )
    
    def test_is_sos_change_valid1(self):
        self.assertEqual(
            core.is_sos_change_valid(TestCore.__sog, (1, 2), core.SOS.DARK),
            True
        )

    def test_is_sos_change_valid2(self):
        self.assertEqual(
            core.is_sos_change_valid(TestCore.__sog, (0, 1), core.SOS.LIGHT),
            False
        )
    
    def test_duplicate_sog(self):
        sog2 = core.duplicate_sog(TestCore.__sog)
        self.assertEqual(
            sog2,
            TestCore.__sog
        )
        self.assertFalse(
            id(sog2) == id(TestCore.__sog))

    def test_calc_sog_after_sos_changed1(self):
        sog2 = [ \
            [core.SOS.BLANK, core.SOS.DARK , core.SOS.LIGHT, core.SOS.DARK ,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK, core.SOS.BLANK, core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK] \
        ]
        self.assertEqual(
            core.calc_sog_after_sos_changed(TestCore.__sog, (1, 2), core.SOS.DARK),
            sog2
        )

    def test_calc_sog_after_sos_changed2(self):
        self.assertEqual(
            core.calc_sog_after_sos_changed(TestCore.__sog, (1, 2), core.SOS.BLANK),
            TestCore.__sog
        )

    def test_count_soss(self):
        self.assertEqual(
            core.count_soss(TestCore.__sog),
            (7, 3, 6)
        )
    
    def test_get_positions_in_sos(self):
        self.assertEqual(
            core.get_positions_in_sos(self.__sog, core.SOS.BLANK),
            [(0, 0), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        )

    def test_sog_to_string(self):
        self.assertEqual(
            core.sog_to_string(TestCore.__sog),
            TestCore.__sog_str
        )

    def test_string_to_sog(self):
        self.assertEqual(
            core.string_to_sog(TestCore.__sog_str),
            TestCore.__sog
        )

class TestCoreDisk(unittest.TestCase):
    def test_toSOS(self):
        self.assertEqual(
            core.Disk.toSOS(core.Disk.DARK),
            core.SOS.DARK
        )

if __name__ == "__main__":
    unittest.main()

# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero import core

class TestCore(unittest.TestCase):
    __SOG = [ \
        [core.SOS.BLANK, core.SOS.DARK , core.SOS.LIGHT, core.SOS.DARK ,], \
        [core.SOS.DARK , core.SOS.LIGHT, core.SOS.BLANK, core.SOS.BLANK,], \
        [core.SOS.DARK , core.SOS.LIGHT, core.SOS.BLANK, core.SOS.BLANK,], \
        [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK] \
    ]

    __SOG_STR = \
        "0,1,-1,1," + \
        "1,-1,0,0," + \
        "1,-1,0,0," + \
        "1,1,1,0"

    def test_calc_sid1(self):
        self.assertEqual(
            core.calc_sid(self.__SOG, (1, 2), core.SOS.DARK, core.Direction.LOW_L),
            1
        )

    def test_calc_sid2(self):
        self.assertEqual(
            core.calc_sid(self.__SOG, (1, 2), core.SOS.BLANK, core.Direction.LOW_L),
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
            core.calc_all_sids(self.__SOG, (1, 2), core.SOS.DARK),
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
            core.is_sos_change_valid(self.__SOG, (1, 2), core.SOS.DARK),
            True
        )

    def test_is_sos_change_valid2(self):
        self.assertEqual(
            core.is_sos_change_valid(self.__SOG, (0, 1), core.SOS.LIGHT),
            False
        )
    
    def test_duplicate_sog(self):
        sog2 = core.duplicate_sog(self.__SOG)
        self.assertEqual(
            sog2,
            self.__SOG
        )
        self.assertFalse(
            id(sog2) == id(self.__SOG))

    def test_calc_sog_after_sos_changed1(self):
        sog2 = [ \
            [core.SOS.BLANK, core.SOS.DARK , core.SOS.LIGHT, core.SOS.DARK ,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK, core.SOS.BLANK, core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK] \
        ]
        self.assertEqual(
            core.calc_sog_after_sos_changed(self.__SOG, (1, 2), core.SOS.DARK),
            sog2
        )

    def test_calc_sog_after_sos_changed2(self):
        self.assertEqual(
            core.calc_sog_after_sos_changed(self.__SOG, (1, 2), core.SOS.BLANK),
            self.__SOG
        )

    def test_count_soss(self):
        self.assertEqual(
            core.count_soss(self.__SOG),
            (7, 3, 6)
        )
    
    def test_get_positions_in_sos(self):
        self.assertEqual(
            core.get_positions_in_sos(self.__SOG, core.SOS.BLANK),
            [(0, 0), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        )

    def test_sog_to_string(self):
        self.assertEqual(
            core.sog_to_string(self.__SOG),
            self.__SOG_STR
        )

    def test_string_to_sog(self):
        self.assertEqual(
            core.string_to_sog(self.__SOG_STR),
            self.__SOG
        )

class TestCoreDisk(unittest.TestCase):
    def test_toSOS(self):
        self.assertEqual(
            core.Disk.toSOS(core.Disk.DARK),
            core.SOS.DARK
        )

if __name__ == "__main__":
    unittest.main()

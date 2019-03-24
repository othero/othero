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

    def test_calcSID(self):
        self.assertEqual(
            core.calcSID(TestCore.__sog, (1, 2), core.SOS.DARK, core.Direction.LOW_L),
            1
        )
        self.assertEqual(
            core.calcSID(TestCore.__sog, (1, 2), core.SOS.BLANK, core.Direction.LOW_L),
            0
        )

    def test_calcAllSIDs(self):
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
            core.calcAllSIDs(TestCore.__sog, (1, 2), core.SOS.DARK),
            expect
        )
    
    def test_advancePos(self):
        self.assertEqual(
            core.advancePos((1, 2), core.Direction.LOW_L, 2),
            (3, 0)
        )

    def test_isInBoard(self):
        self.assertEqual(
            core.isInBoard((1, 2)),
            True
        )
        self.assertEqual(
            core.isInBoard((4, 0)),
            False
        )
    
    def test_isSOSChangeValid(self):
        self.assertEqual(
            core.isSOSChangeValid(TestCore.__sog, (1, 2), core.SOS.DARK),
            True
        )
        self.assertEqual(
            core.isSOSChangeValid(TestCore.__sog, (0, 1), core.SOS.LIGHT),
            False
        )
    
    def test_duplicateSOG(self):
        sog2 = core.duplicateSOG(TestCore.__sog)
        self.assertEqual(
            sog2,
            TestCore.__sog
        )
        self.assertFalse(
            id(sog2) == id(TestCore.__sog))

    def test_calcSOGAfterSOSChanged(self):
        sog2 = [ \
            [core.SOS.BLANK, core.SOS.DARK , core.SOS.LIGHT, core.SOS.DARK ,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK, core.SOS.BLANK, core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK] \
        ]
        self.assertEqual(
            core.calcSOGAfterSOSChanged(TestCore.__sog, (1, 2), core.SOS.DARK),
            sog2
        )
        self.assertEqual(
            core.calcSOGAfterSOSChanged(TestCore.__sog, (1, 2), core.SOS.BLANK),
            TestCore.__sog
        )

    def test_countSOSs(self):
        self.assertEqual(
            core.countSOSs(TestCore.__sog),
            (7, 3, 6)
        )

    def test_SOGToString(self):
        self.assertEqual(
            core.SOGToString(TestCore.__sog),
            TestCore.__sog_str
        )

    def test_stringToSOG(self):
        self.assertEqual(
            core.stringToSOG(TestCore.__sog_str),
            TestCore.__sog
        )

if __name__ == "__main__":
    unittest.main()

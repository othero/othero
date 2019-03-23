# coding: utf-8

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

    def test_putDiskAndReverse(self):
        sog2 = [ \
            [core.SOS.BLANK, core.SOS.DARK , core.SOS.LIGHT, core.SOS.DARK ,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK, core.SOS.BLANK, core.SOS.BLANK,], \
            [core.SOS.DARK , core.SOS.DARK , core.SOS.DARK , core.SOS.BLANK] \
        ]
        self.assertEqual(
            core.putDiskAndReverse(TestCore.__sog, (1, 2), core.SOS.DARK),
            sog2
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

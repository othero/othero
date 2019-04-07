# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test.testutils import Test2

from othero.core import libsog, libtypes

class TestCoreSogSOG(unittest.TestCase):
    __SOG_STR = \
        "0,1,-1,1," + \
        "1,0," + \
        "1,0," + \
        "1,1,1,0"

    def test_duplicate(self):
        sog2 = Test2.SOG.duplicate()
        self.assertEqual(sog2, Test2.SOG)
        sog2.setSos((1, 3), libtypes.SOS.LIGHT)
        self.assertNotEqual(sog2, Test2.SOG)

    def test_getSos(self):
        self.assertEqual(
            Test2.SOG.getSos((1, 3)),
            libtypes.SOS.BLANK
        )

    def test_create_sog(self):
        _STENCIL = [
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True]
        ]
        _DARKS = [(1, 1), (2, 2)]
        _LIGHTS = [(1, 2), (2, 1)]
        _DEFAULT_SOG = libsog.SOG(_STENCIL, _DARKS, _LIGHTS)
        self.assertEqual(
            libsog.create_sog(),
            _DEFAULT_SOG
        )
        self.assertNotEqual(
            id(libsog.create_sog()),
            id(_DEFAULT_SOG)
        )

    def test_isInside1(self):
        self.assertEqual(
            Test2.SOG.isInside((1, 3)),
            True
        )

    def test_isInside2(self):
        self.assertEqual(
            Test2.SOG.isInside((4, 0)),
            False
        )

    def test_isInside3(self):
        self.assertEqual(
            Test2.SOG.isInside((1, 2)),
            False
        )

    def test_countSoss(self):
        self.assertEqual(
            Test2.SOG.countSoss(),
            (7, 1, 4)
        )

    def test_getPositionsInSos(self):
        self.assertEqual(
            Test2.SOG.getPositionsInSos(libtypes.SOS.BLANK),
            [(0, 0), (1, 3), (2, 3), (3, 3)]
        )

    def test_toString(self):
        self.assertEqual(
            Test2.SOG.toString(),
            self.__SOG_STR
        )

    def test_initFromString(self):
        sog = libsog.SOG(Test2.STENCIL)
        sog.initFromString(self.__SOG_STR)
        self.assertEqual(sog, Test2.SOG)

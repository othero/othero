# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test.testutils import Test1

from othero.core import libtypes
from othero.rule import utils

class TestRuleUtils(unittest.TestCase):
    def test_calc_sid1(self):
        self.assertEqual(
            utils.calc_sid(Test1.SOG, (1, 2), libtypes.SOS.DARK, libtypes.Direction.LOW_L),
            1
        )

    def test_calc_sid2(self):
        self.assertEqual(
            utils.calc_sid(Test1.SOG, (1, 2), libtypes.SOS.BLANK, libtypes.Direction.LOW_L),
            0
        )

    def test_calc_all_sids(self):
        expect = {
            libtypes.Direction.UP: 0,
            libtypes.Direction.UP_R: 0,
            libtypes.Direction.RIGHT: 0,
            libtypes.Direction.LOW_R: 0,
            libtypes.Direction.LOW: 0,
            libtypes.Direction.LOW_L: 1,
            libtypes.Direction.LEFT: 1,
            libtypes.Direction.UP_L: 0
        }
        self.assertEqual(
            utils.calc_all_sids(Test1.SOG, (1, 2), libtypes.SOS.DARK),
            expect
        )

    def test_calc_sidb1(self):
        self.assertEqual(
            utils.calc_sidb(Test1.SOG, (1, 2), libtypes.Direction.LOW_R),
            0
        )

    def test_calc_sidb2(self):
        self.assertEqual(
            utils.calc_sidb(Test1.SOG, (1, 0), libtypes.Direction.LOW),
            1
        )

    def test_calc_all_sidbs(self):
        expect = {
            libtypes.Direction.UP: 0,
            libtypes.Direction.UP_R: 0,
            libtypes.Direction.RIGHT: 0,
            libtypes.Direction.LOW_R: 0,
            libtypes.Direction.LOW: 1,
            libtypes.Direction.LOW_L: 0,
            libtypes.Direction.LEFT: 0,
            libtypes.Direction.UP_L: 0
        }
        self.assertEqual(
            utils.calc_all_sidbs(Test1.SOG, (1, 0)),
            expect
        )

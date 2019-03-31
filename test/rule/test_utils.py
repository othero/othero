# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import types
from othero.rule import utils

class TestRuleUtils(unittest.TestCase):
    __SOG = [ \
        [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
    ]

    def test_calc_sid1(self):
        self.assertEqual(
            utils.calc_sid(self.__SOG, (1, 2), types.SOS.DARK, types.Direction.LOW_L),
            1
        )

    def test_calc_sid2(self):
        self.assertEqual(
            utils.calc_sid(self.__SOG, (1, 2), types.SOS.BLANK, types.Direction.LOW_L),
            0
        )

    def test_calc_all_sids(self):
        expect = {
            types.Direction.UP: 0,
            types.Direction.UP_R: 0,
            types.Direction.RIGHT: 0,
            types.Direction.LOW_R: 0,
            types.Direction.LOW: 0,
            types.Direction.LOW_L: 1,
            types.Direction.LEFT: 1,
            types.Direction.UP_L: 0
        }
        self.assertEqual(
            utils.calc_all_sids(self.__SOG, (1, 2), types.SOS.DARK),
            expect
        )
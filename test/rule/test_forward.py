# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import types
from othero.rule import forward

class TestRuleForward(unittest.TestCase):
    __SOG = [ \
        [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
    ]

    def test_is_sos_change_valid1(self):
        self.assertEqual(
            forward.is_sos_change_valid(self.__SOG, (1, 2), types.SOS.DARK),
            True
        )

    def test_is_sos_change_valid2(self):
        self.assertEqual(
            forward.is_sos_change_valid(self.__SOG, (0, 1), types.SOS.LIGHT),
            False
        )

    def test_calc_sog_after_sos_changed1(self):
        sog2 = [ \
            [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
            [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK,], \
            [types.SOS.DARK , types.SOS.DARK, types.SOS.BLANK, types.SOS.BLANK,], \
            [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
        ]
        self.assertEqual(
            forward.calc_sog_after_sos_changed(self.__SOG, (1, 2), types.SOS.DARK),
            sog2
        )

    def test_calc_sog_after_sos_changed2(self):
        self.assertEqual(
            forward.calc_sog_after_sos_changed(self.__SOG, (1, 2), types.SOS.BLANK),
            self.__SOG
        )
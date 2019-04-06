# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test import testutils
from test.testutils import Test1

from othero.core import libtypes
from othero.rule import libforward

class TestRuleForward(unittest.TestCase):
    def test_is_sos_change_valid1(self):
        self.assertEqual(
            libforward.is_sos_change_valid(Test1.SOG, (1, 2), libtypes.SOS.DARK),
            True
        )

    def test_is_sos_change_valid2(self):
        self.assertEqual(
            libforward.is_sos_change_valid(Test1.SOG, (0, 1), libtypes.SOS.LIGHT),
            False
        )

    def test_calc_sog_after_sos_changed1(self):
        SOSSS2 = [
            [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.BLANK],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
        ]
        SOG2 = testutils.sosss_to_sog(SOSSS2)
        self.assertEqual(
            libforward.calc_sog_after_sos_changed(Test1.SOG, (1, 2), libtypes.SOS.DARK),
            SOG2
        )

    def test_calc_sog_after_sos_changed2(self):
        self.assertEqual(
            libforward.calc_sog_after_sos_changed(Test1.SOG, (1, 2), libtypes.SOS.BLANK),
            Test1.SOG
        )

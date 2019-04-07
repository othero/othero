# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test import testutils
from test.testutils import Test1

from othero.core import libtypes, libsog
from othero.game import utils

class TestGameUtils(unittest.TestCase):
    def test_calc_sog_after_put_disk(self):
        SOSSS2 = [
            [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.BLANK],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
        ]
        SOG2 = testutils.sosss_to_sog(SOSSS2)
        self.assertEqual(
            utils.calc_sog_after_put_disk(Test1.SOG, (1, 2), libtypes.Disk.DARK),
            SOG2
        )
    
    def test_is_put_disk_valid1(self):
        self.assertEqual(
            utils.is_put_disk_valid(Test1.SOG, (1, 2), libtypes.Disk.DARK),
            True
        )

    def test_is_put_disk_valid2(self):
        self.assertEqual(
            utils.is_put_disk_valid(Test1.SOG, (1, 2), libtypes.Disk.LIGHT),
            False
        )

class TestGameUtilsGame(unittest.TestCase):
    pass

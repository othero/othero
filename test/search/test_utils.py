# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test import testutils

from othero.core import libtypes
from othero.search import utils

class TestSearchUtils(unittest.TestCase):
    def test_get_winner_disk(self):
        SOG = testutils.sosss_to_sog([
            [libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.DARK],
            [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.DARK],
            [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK]
        ])

        self.assertEqual(
            utils.get_winner_disk(SOG),
            libtypes.Disk.DARK
        )

# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libtypes
from othero.search import libfws

class TestSearchFws(unittest.TestCase):
    __SOG = [
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.BLANK, libtypes.SOS.DARK ],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
    ]

    def test_get_available_positions(self):
        self.assertEqual(
            libfws.get_available_positions(self.__SOG, libtypes.Disk.DARK),
            [(0, 2), (1, 2), (2, 2)]
        )

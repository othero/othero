# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest
from othero.core import libtypes

class TestCoreTypesDisk(unittest.TestCase):
    def test_toSOS(self):
        self.assertEqual(
            libtypes.Disk.toSOS(libtypes.Disk.DARK),
            libtypes.SOS.DARK
        )
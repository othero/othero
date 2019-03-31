# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest
from othero.core import types

class TestCoreTypesDisk(unittest.TestCase):
    def test_toSOS(self):
        self.assertEqual(
            types.Disk.toSOS(types.Disk.DARK),
            types.SOS.DARK
        )
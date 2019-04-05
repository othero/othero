# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libdisk, libtypes

class TestCoreDisk(unittest.TestCase):
    def test_next_disk(self):
        self.assertEqual(
            libdisk.next_disk(libtypes.Disk.DARK),
            libtypes.Disk.LIGHT
        )

    def test_prev_disk(self):
        self.assertEqual(
            libdisk.prev_disk(libtypes.Disk.DARK),
            libtypes.Disk.LIGHT
        )

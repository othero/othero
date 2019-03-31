# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libpos, libtypes

class TestCorePos(unittest.TestCase):
    def test_advance_pos(self):
        self.assertEqual(
            libpos.advance_pos((1, 2), libtypes.Direction.LOW_L, 2),
            (3, 0)
        )
    
    def test_is_in_board1(self):
        self.assertEqual(
            libpos.is_in_board((1, 2)),
            True
        )

    def test_is_in_board2(self):
        self.assertEqual(
            libpos.is_in_board((4, 0)),
            False
        )

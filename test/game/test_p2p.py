# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest
from othero import core
from othero.game import p2p

class TestGameP2P(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(
            p2p.parse(" (1, 0 )"),
            (1, 0)            
        )

if __name__ == "__main__":
    unittest.main()
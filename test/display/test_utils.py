# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import types
from othero.display import utils

class TestDisplayUtils(unittest.TestCase):
    __SOG = [ \
        [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK]   \
    ]
    __VSOG = [ \
        [' ', 'x', 'o', 'x',], \
        ['x', 'o', ' ', ' ',], \
        ['x', 'o', ' ', ' ',], \
        ['x', 'x', 'x', ' ']   \
    ]

    def test_visualize_sos1(self):
        self.assertEqual(
            utils.visualize_sos(types.SOS.DARK),
            'x'
        )

    def test_visualize_sos2(self):
        self.assertEqual(
            utils.visualize_sos(types.SOS.LIGHT),
            'o'
        )

    def test_visualize_sos3(self):
        self.assertEqual(
            utils.visualize_sos(types.SOS.BLANK),
            ' '
        )

    def test_visualize_sog(self):
        self.assertEqual(
            utils.visualize_sog(self.__SOG),
            self.__VSOG
        )

if __name__ == "__main__":
    unittest.main()

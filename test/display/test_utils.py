# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libtypes
from othero.display import utils

class TestDisplayUtils(unittest.TestCase):
    __SOG = [ \
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]   \
    ]
    __VSOG = [ \
        [' ', 'x', 'o', 'x',], \
        ['x', 'o', ' ', ' ',], \
        ['x', 'o', ' ', ' ',], \
        ['x', 'x', 'x', ' ']   \
    ]

    def test_visualize_sos1(self):
        self.assertEqual(
            utils.visualize_sos(libtypes.SOS.DARK),
            'x'
        )

    def test_visualize_sos2(self):
        self.assertEqual(
            utils.visualize_sos(libtypes.SOS.LIGHT),
            'o'
        )

    def test_visualize_sos3(self):
        self.assertEqual(
            utils.visualize_sos(libtypes.SOS.BLANK),
            ' '
        )

    def test_visualize_sog(self):
        self.assertEqual(
            utils.visualize_sog(self.__SOG),
            self.__VSOG
        )

if __name__ == "__main__":
    unittest.main()

# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import sog, types

class TestCoreSog(unittest.TestCase):
    __SOG = [ \
        [types.SOS.BLANK, types.SOS.DARK , types.SOS.LIGHT, types.SOS.DARK ,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK, types.SOS.BLANK,], \
        [types.SOS.DARK , types.SOS.DARK , types.SOS.DARK , types.SOS.BLANK] \
    ]

    __SOG_STR = \
        "0,1,-1,1," + \
        "1,-1,0,0," + \
        "1,-1,0,0," + \
        "1,1,1,0"

    def test_duplicate_sog(self):
        sog2 = sog.duplicate_sog(self.__SOG)
        self.assertEqual(
            sog2,
            self.__SOG
        )
        self.assertFalse(
            id(sog2) == id(self.__SOG))

    def test_sog_to_string(self):
        self.assertEqual(
            sog.sog_to_string(self.__SOG),
            self.__SOG_STR
        )

    def test_string_to_sog(self):
        self.assertEqual(
            sog.string_to_sog(self.__SOG_STR),
            self.__SOG
        )

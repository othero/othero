# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libsog, libtypes

class TestCoreSog(unittest.TestCase):
    __SOG = [ \
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK] \
    ]

    __SOG_STR = \
        "0,1,-1,1," + \
        "1,-1,0,0," + \
        "1,-1,0,0," + \
        "1,1,1,0"

    def test_duplicate_sog(self):
        sog2 = libsog.duplicate_sog(self.__SOG)
        self.assertEqual(
            sog2,
            self.__SOG
        )
        self.assertFalse(
            id(sog2) == id(self.__SOG))

    def test_get_sos_at_pos(self):
        self.assertEqual(
            libsog.get_sos_at_pos(self.__SOG, (1, 2)),
            libtypes.SOS.BLANK
        )

    def test_is_pos_inside_sog1(self):
        self.assertEqual(
            libsog.is_pos_inside_sog(self.__SOG, (1, 2)),
            True
        )

    def test_is_pos_inside_sog2(self):
        self.assertEqual(
            libsog.is_pos_inside_sog(self.__SOG, (4, 0)),
            False
        )

    def test_sog_to_string(self):
        self.assertEqual(
            libsog.sog_to_string(self.__SOG),
            self.__SOG_STR
        )

    def test_init_sog_from_string(self):
        sog = [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]
        libsog.init_sog_from_string(sog, self.__SOG_STR)
        self.assertEqual(sog, self.__SOG)

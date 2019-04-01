# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from othero.core import libtypes
from othero.rule import libbackward

class TestRuleBackward(unittest.TestCase):
    __SOG = [ \
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK,], \
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK] \
    ]

    def test_is_sos_restore_valid1(self):
        self.assertEqual(
            libbackward.is_sos_restore_valid(self.__SOG, (1, 0)),
            False
        )

    def test_is_sos_restore_valid2(self):
        self.assertEqual(
            libbackward.is_sos_restore_valid(self.__SOG, (3, 0)),
            True
        )

    def test_calc_sogs_after_sos_restored(self):
        def is_equal(x, y):
            return all([a in y for a in x]) \
                    and all([a in x for a in y])

        result = is_equal(
            libbackward.calc_sogs_after_sos_restored(self.__SOG, (3, 0), libtypes.SOS.LIGHT),
            [
                [
                    [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
                    [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                    [libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                    [libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
                ],
                [
                    [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
                    [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                    [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                    [libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.BLANK]
                ],
                [
                    [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
                    [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                    [libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
                    [libtypes.SOS.LIGHT, libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.BLANK]
                ]
            ]
        )
        self.assertTrue(result)
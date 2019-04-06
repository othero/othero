# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test import testutils
from test.testutils import Test2

class TestTestutils(unittest.TestCase):
    def test_sosss_to_sog(self):
        self.assertEqual(
            testutils.sosss_to_sog(Test2.SOSSS),
            Test2.SOG
        )
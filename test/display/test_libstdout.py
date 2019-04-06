# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import unittest

from test.testutils import Test1

from othero.core import libtypes
from othero.display import libstdout

class TestDisplayStdout(unittest.TestCase):
    def test_display_sog_to_shell(self):
        libstdout.display_sog_to_shell(Test1.SOG)

if __name__ == "__main__":
    unittest.main()
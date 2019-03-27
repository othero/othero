# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero import core
from othero.display import utils

def display_sog_to_shell(sog):
    """
    Display othero.core.SOG to the shell.

    Args:
        sog othero.core.SOG:
            Sog to display.

    Returns:
        [[str]]:
            Resulting list from <sos>.
    """
    vsog = utils.visualize_sog(sog)
    print('+-+-+-+-+')
    for row in vsog:
        print('|', end="")
        for vsos in row:
            print(vsos, end="")
            print('|', end="")
        print('\n', end="")
    print('+-+-+-+-+')

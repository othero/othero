# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes

""" NOTE
SOG:
    SOG is a two-dimentional array. The first dimention indicates a
    row, and the second indicates a collumn. For example, SOG[i][j]
    represents the sos in the intersection of i-th row and j-th collumn.
"""

DEFAULT_SOG = [
        [libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK],
        [libtypes.SOS.BLANK, libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.BLANK],
        [libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK, libtypes.SOS.BLANK]
    ]

def create_sog():
    return duplicate_sog(DEFAULT_SOG)

def duplicate_sog(sog):
    """
    Make a full copy (ie. deep copy) of <sog>.

    Args:
        sog [[othero.core.libtypes.SOS]]:
            State of the game to be copied.
    
    Return:
        [[othero.core.libtypes.SOS]]:
            State of the game that is newly created.
    """
    return [[sos for sos in row] for row in sog]

def get_sos_at_pos(sog, pos):
    """
    Return a sos at <pos> in <sog>.

    Args:
        sog [[othero.core.libtypes.SOS]]:

        pos (int, int):

    Returns:
        othero.core.libtypes.SOS:

    """
    return sog[pos[0]][pos[1]]

def sog_to_string(sog):
    """
    Convert state of a game into string.

    This method is intended to be used to serialize state of a
    game so that it can be passed to another program.

    Args:
        sog [[othero.core.libtypes.SOS]]:
            State of a game to be converted.
    
    Returns:
        string:
            Resulting string from <sog>.
    """
    ps = [p for row in sog for p in row]
    s = ""
    for p in map(int, ps):
        s = s + "," + str(p)
    return s[1:]

def string_to_sog(s):
    """
    Convert string to state of a game.

    This method is intended to be used to deserialize state of a
    game passed from another program so that it can be used inside
    of this program.

    Args:
        s string:
            String to be converted.
    
    Returns:
        [[othero.core.libtypes.SOS]]:
            Resulting sos from <s>.
    """
    ps = list(map(int, s.split(',')))
    return [[ps[i+j*4] for i in range(4)] for j in range(4)]

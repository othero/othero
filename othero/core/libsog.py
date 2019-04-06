# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

""" NOTE
SOG:
    SOG is a two-dimentional array. The first dimention indicates a
    row, and the second indicates a collumn. For example, SOG[i][j]
    represents the sos in the intersection of i-th row and j-th collumn.
"""

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

def is_pos_inside_sog(sog, pos):
    """
    Check whether the position indicated by <pos> is within
    the board of a game.

    Args:
        sog [[othero.core.libtypes.SOS]]:

        pos (int, int):
            Position to be checked.

            The int values represent row and collumn number
            respectively. They begin from 0.
    
    Returns:
        bool:
            Whether the position is within the board of a game.
            True: inside
            False: outside
    """
    if pos[0] not in range(len(sog)):
        return False

    row = sog[pos[0]]
    if pos[1] not in range(len(row)):
        return False

    return True

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

def init_sog_from_string(sog, s):
    """
    Initialize <sog> with <s>.

    This method is intended to be used to deserialize state of a
    game passed from another program so that it can be used inside
    of this program.

    Args:
        sog [[othero.core.libtypes.SOS]]:
            Sog to be initialized.

        s string:
            String to be converted.
    """
    ps = list(map(int, s.split(',')))
    i = 0
    for row in range(len(sog)):
        for col in range(len(sog[row])):
            if i < len(ps):
                sog[row][col] = ps[i]
            else:
                sog[row][col] = None
            i += 1

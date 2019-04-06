# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes, libpos, libsog

""" NOTE
SID:
    SID is a number representing how many disks will be reversed
    when the state of the square at the certain position is changed.

    SID is calculated in each direction relative to the changed square.

    The number of SID means:
        0: no disk will be reversed
        n: n disks will be reversed
"""

def calc_sid(sog, pos, sos, direction):
    """
    Calculate SID in the direction specified by <direction>.

    Args: 
        sog othero.core.libsog.SOG:
            State of the game.

        pos (int, int):
            Position where the sos changes.

            The int values represent row and collumn number
            respectively. They begin from 0.

        sos othero.core.libtypes.SOS:
            Sos which the square is to be in.

        direction othero.core.libtypes.Direction:
            Direction in which the sid should be calculated.

    Returns:
        int:
            State in the direction of <direction>.
    """
    if sos == libtypes.SOS.BLANK:
        return 0

    sid = 0
    while True:
        pos = libpos.advance_pos(pos, direction)

        if not sog.isInside(pos):
            sid = 0
            break
            
        s = sog.getSos(pos)
        if s == libtypes.SOS.BLANK:
            sid = 0
            break
        elif s == sos:
            break
        else:
            sid = sid + 1

    return sid

def calc_all_sids(sog, pos, sos):
    """
    Returns a map of 8 numbers representing SID in each direction.
    SID in a direction can be accessed with the corresponding direction
    constant.

    Args: 
        sog othero.core.libsog.SOG:
            State of the game.

        pos (int, int):
            Position where the sos changes.

            The int values represent row and collumn number
            respectively. They begin from 0.

        sos othero.core.libtypes.SOS:
            Sos which the square is to be in.

    Returns:
        {othero.core.libtypes.Direction: int}:
            State in each direction.
    
    Example:
        msid = callAllSIDs(sog, pos, sos)
        if msid[othero.core.libtypes.Direction.RIGHT] == 2:
            print("Two disks are reversed in the right of the new disk")
    """
    sids = {}
    for d in list(libtypes.Direction):
        sids[d] = calc_sid(sog, pos, sos, d)
    return sids
# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes, libpos

""" NOTE
SID:
    SID is a number representing how many disks will be reversed
    when the state of the square at the certain position is changed.

    SID is calculated in each direction relative to the changed square.

    The number of SID means:
        0: no disk will be reversed
        n: n disks will be reversed

SIDB:
    SIDB is a number representing up to how many disks can be restored along with
    a restoration of the state of the square at a certain position.

    SIDB is calculated in each direction relative to the restored square.

    The number of SIDB means:
        0: no disk will be restored
        n: up to n disks will be restored
"""

def calc_sid(sog, pos, sos, direction):
    """
    Calculate SID in the direction specified by <direction>.

    Args: 
        sog [[othero.core.libtypes.SOS]]:
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

        if not libpos.is_in_board(pos):
            sid = 0
            break

        s = sog[pos[0]][pos[1]]
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
        sog [[othero.core.libtypes.SOS]]:
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

def calc_sidb(sog, pos, direction):
    """
    Calculate SIDB in the direction specified by <direction>.

    Args: 
        sog [[othero.core.SOS]]:

        pos (int, int):

        direction othero.core.Direction:

    Returns:
        int:
            State in the direction of <direction>.
    """
    sos = sog[pos[0]][pos[1]]
    if sos == libtypes.SOS.BLANK:
        return 0

    sidb = 0 
    while True:
        pos = libpos.advance_pos(pos, direction)

        if not libpos.is_in_board(pos):
            break

        s = sog[pos[0]][pos[1]]        
        if s == sos:
            sidb += 1
        else:
            break

    if sidb != 0:
        sidb -= 1

    return sidb

def calc_all_sidbs(sog, pos):
    """
    Returns a map of 8 numbers representing SID in each direction.
    SID in a direction can be accessed with the corresponding direction
    constant.

    Args:
        sog [[othero.core.libtypes.SOS]]:

        pos (int, int):

    Returns:
        {othero.core.Direction: int}: 
            State in each direction.
    """
    sidbs = {}
    for d in list(libtypes.Direction):
        sidbs[d] = calc_sidb(sog, pos, d)
    return sidbs
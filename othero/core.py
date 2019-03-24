# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

__version__ = "0.00"
__date__    = "23 Mar 2019"

import string
import enum

""" NOTE
Terms: 
    sog: state of a game
    sos: state of a square
    sid: state in a direction

SOG:
    SOG is a two-dimentional array. The first dimention indicates a
    row, and the second indicates a collumn. For example, SOG[i][j]
    represents the sos in the intersection of i-th row and j-th collumn.

SID:
    SID is a number representing how many disks will be reversed
    when the state of the square at the certain position is changed.

    SID is calculated in each direction relative to the changed square.

    The number of SID means:
        0: no disk will be reversed
        n: n disks will be reversed
"""

class SOS(enum.IntEnum):
    """
    State of squares(SOS)
    """
    DARK  =  1
    LIGHT = -1
    BLANK =  0

class Direction(enum.Flag):
    """
    Direction constant
    """
    UP    = enum.auto()
    LOW   = enum.auto()
    RIGHT = enum.auto()
    LEFT  = enum.auto()
    UP_R  = UP |RIGHT
    LOW_R = LOW|RIGHT
    UP_L  = UP |LEFT
    LOW_L = LOW|LEFT

# This variable means amount of change 'xy-coordinate' by one step.
__posSteps = {
    Direction.UP   : (-1,  0),
    Direction.UP_R : (-1,  1),
    Direction.RIGHT: ( 0,  1),
    Direction.LOW_R: ( 1,  1),
    Direction.LOW  : ( 1,  0),
    Direction.LOW_L: ( 1, -1),
    Direction.LEFT : ( 0, -1),
    Direction.UP_L : (-1, -1)
}

def calcSID(sog, pos, sos, direction):
    """
    Calculate SID in the direction specified by <direction>.

    Args: 
        sog [[othero.core.SOS]]:
            State of the game.

        pos (int, int):
            Position where the sos changes.

            The int values represent row and collumn number
            respectively. They begin from 0.

        sos othero.core.SOS:
            Sos which the square is to be in.

        direction othero.core.Direction:
            Direction in which the sid should be calculated.

    Returns:
        int:
            State in the direction of <direction>.
    """
    if sos == SOS.BLANK:
        return 0

    sid = 0
    while True:
        pos = advancePos(pos, direction)

        if not isInBoard(pos):
            sid = 0
            break
            
        s = sog[pos[0]][pos[1]]
        if s == SOS.BLANK:
            sid = 0
            break
        elif s == sos:
            break
        else:
            sid = sid + 1

    return sid

def calcAllSIDs(sog, pos, sos):
    """
    Returns a map of 8 numbers representing SID in each direction.
    SID in a direction can be accessed with the corresponding direction
    constant.

    Args: 
        sog [[othero.core.SOS]]:
            State of the game.

        pos (int, int):
            Position where the sos changes.

            The int values represent row and collumn number
            respectively. They begin from 0.

        sos othero.core.SOS:
            Sos which the square is to be in.

    Returns:
        {othero.core.Direction: int}:
            State in each direction.
    
    Example:
        msid = callAllSIDs(sog, pos, sos)
        if msid[othero.core.Direction.RIGHT] == 2:
            print("Two disks are reversed in the right of the new disk")
    """
    sids = {}
    for d in list(Direction):
        sids[d] = calcSID(sog, pos, sos, d)
    return sids

def advancePos(pos, direction, nsteps=1):
    """
    Advance pos in the <direction> by <nsteps> steps, and
    return a new position.

    Args: 
        pos (int, int):
            Position in a board.

            The int values represent row and collumn number
            respectively. They begin from 0.
        
        direction othero.core.Direction:
            Direction in which pos advances.

        nsteps int = 1:
            Number of steps by which <pos> advances.

    Returns:
        (int, int):
            New position in a board after advance.
    """
    step = __posSteps[direction]
    return (pos[0]+step[0]*nsteps, pos[1]+step[1]*nsteps)

def isInBoard(pos):
    """
    Check whether the position indicated by <pos> is within
    the board of a game.

    Args:
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
    return pos[0] >= 0 and pos[0] < 4 and \
           pos[1] >= 0 and pos[1] < 4

def isSOSChangeValid(sog, pos, sos):
    """
    Checks whether the sos change is allowed by osero rule.

    Args:
        sog [[othero.core.SOS]]:
            State of a game to be converted.

        pos (int, int):
            Position where the sos changes.

            The int values represent row and collumn number
            respectively. They begin from 0.
        
        sos othero.core.SOS:
            Sos which the square is to be in.
    
    Returns:
        bool:
            Resulting sos from <s>.
    """
    return any(map(bool, calcAllSIDs(sog, pos, sos).values())) 

def duplicateSOG(sog):
    """
    Make a full copy (ie. deep copy) of <sog>.

    Args:
        sog [[othero.core.SOS]]:
            State of the game to be copied.
    
    Return:
        [[othero.core.SOS]]:
            State of the game that is newly created.
    """
    return [[sos for sos in row] for row in sog]
    
def calcSOGAfterSOSChanged(sog, pos, sos):
    """
    Put a <sos>'s disk on the <pos> and change the all <sog> around <pos>.

    Args: 
        sog [[othero.core.SOS]]:
            State of the game.:w

        pos (int, int):
            Position where the sos changes.

            The int values represent row and collumn number
            respectively. They begin from 0.

        sos othero.core.SOS:
            Sos which the square is to be in.

    Returns:
        sog [[othero.core.SOS]]:
            Return the new state of the game after putDiskAndChange method.

    """
    new_sog = duplicateSOG(sog)
    sids = calcAllSIDs(new_sog, pos, sos)
    new_sog[pos[0]][pos[1]] = sos
    for direction, sid in sids.items():
        for i in range(sid):
            row, col = advancePos(pos, direction, i+1)
            new_sog[row][col] = sos
    return new_sog

def SOGToString(sog):
    """
    Convert state of a game into string.

    This method is intended to be used to serialize state of a
    game so that it can be passed to another program.

    Args:
        sog [[othero.core.SOS]]:
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

def stringToSOG(s):
    """
    Convert string to state of a game.

    This method is intended to be used to deserialize state of a
    game passed from another program so that it can be used inside
    of this program.

    Args:
        s string:
            String to be converted.
    
    Returns:
        [[othero.core.SOS]]:
            Resulting sos from <s>.
    """
    ps = list(map(int, s.split(',')))
    return [[ps[i+j*4] for i in range(4)] for j in range(4)]

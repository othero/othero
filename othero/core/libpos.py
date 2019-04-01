# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes

# This variable means amount of change 'xy-coordinate' by one step.
__POS_STEPS = {
    libtypes.Direction.UP   : (-1,  0),
    libtypes.Direction.UP_R : (-1,  1),
    libtypes.Direction.RIGHT: ( 0,  1),
    libtypes.Direction.LOW_R: ( 1,  1),
    libtypes.Direction.LOW  : ( 1,  0),
    libtypes.Direction.LOW_L: ( 1, -1),
    libtypes.Direction.LEFT : ( 0, -1),
    libtypes.Direction.UP_L : (-1, -1)
}

def advance_pos(pos, direction, nsteps=1):
    """
    Advance pos in the <direction> by <nsteps> steps, and
    return a new position.

    Args: 
        pos (int, int):
            Position in a board.

            The int values represent row and collumn number
            respectively. They begin from 0.
        
        direction othero.core.libtypes.Direction:
            Direction in which pos advances.

        nsteps int = 1:
            Number of steps by which <pos> advances.

    Returns:
        (int, int):
            New position in a board after advance.
    """
    step = __POS_STEPS[direction]
    return (pos[0]+step[0]*nsteps, pos[1]+step[1]*nsteps)
    
def is_in_board(pos):
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
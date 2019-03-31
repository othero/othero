# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero import core
from othero.core import sog
from othero.rule import utils

def is_sos_change_valid(sog, pos, sos):
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
            Validity of changing <sos>.
    """
    return any(map(bool, utils.calc_all_sids(sog, pos, sos).values())) 

def calc_sog_after_sos_changed(sog, pos, sos):
    """
    Change sos at the <pos> to <sos> and calculate the resulting sog
    according to the osero rule.

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
        sog [[othero.core.SOS]]:
            Return the new state of the game after calcsog_after_sos_changed method.
    """
    new_sog = core.sog.duplicate_sog(sog)
    sids = utils.calc_all_sids(new_sog, pos, sos)
    new_sog[pos[0]][pos[1]] = sos
    for direction, sid in sids.items():
        for i in range(sid):
            row, col = core.pos.advance_pos(pos, direction, i+1)
            new_sog[row][col] = sos
    return new_sog

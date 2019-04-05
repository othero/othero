# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import enum

from othero.core import libboard, libdisk, libtypes
from othero.rule import libforward
from othero.search import utils

def get_available_positions(sog, disk):
    """
    Return a list of positions in <sog> where putting <disk> is allowed.

    Args:
        sog [[othero.core.libtypes.SOS]]:
            Sog to be searched in. 
        
        disk othero.core.libtypes.Disk:
            Disk to be put.
    
    Returns:
        [(int, int)]:
            List of positions in <sog> where putting <disk> is allowed.
    """
    sos = libtypes.Disk.toSOS(disk)

    blank_poss = libboard.get_positions_in_sos(sog, libtypes.SOS.BLANK)
    return [pos for pos in blank_poss \
                if libforward.is_sos_change_valid(sog, pos, sos)]

def calc_all_next_sogs(sog, disk):
    """
    Restore sos at the <pos> to <sos> and calculate the resulting
    possible sogs according to the osero rule.

    Args: 
        sog [[othero.core.libtypes.SOS]]:

        disk othero.core.libtypes.Disk:
            A disk to be put.

    Returns:
        [[[othero.core.libtypes.SOS]]]:
            A list of possible sogs in the next turn. If there is no
            position at which <disk> can be put, the list is empty.
    """
    sos = libtypes.Disk.toSOS(disk)
    return [libforward.calc_sog_after_sos_changed(sog, pos, sos)
                for pos in get_available_positions(sog, disk)]

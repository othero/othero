# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libboard, libtypes
from othero.rule import libforward

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
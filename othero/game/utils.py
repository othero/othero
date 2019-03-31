# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import board, sog, types
from othero.rule import forward
from othero.display import utils

INIT_SOG = [ \
    [types.SOS.BLANK , types.SOS.BLANK, types.SOS.BLANK, types.SOS.BLANK], \
    [types.SOS.BLANK , types.SOS.DARK , types.SOS.LIGHT, types.SOS.BLANK], \
    [types.SOS.BLANK , types.SOS.LIGHT, types.SOS.DARK , types.SOS.BLANK], \
    [types.SOS.BLANK , types.SOS.BLANK, types.SOS.BLANK, types.SOS.BLANK] \
]

class InvalidDiskColorError(Exception):
    def __init__(self, disk):
        self.disk = disk
    
    def __str__(self):
        sdisk = utils.visualize_sos(types.Disk.toSOS(self.disk))
        return f"disk: {sdisk}"

class InvalidDiskPositionError(Exception):
    """
    InvalidDiskPositionError is an exception that occurs
    when putting a disk at a position is not allowed by
    the osero rule.
    """
    def __init__(self, sog, pos, disk):
        self.sog = sog
        self.pos = pos
        self.disk = disk
    
    def __str__(self):
        ssog = utils.visualize_sog(self.sog)
        sdisk = utils.visualize_sos(types.Disk.toSOS(self.disk))
        return f"""
        sog:  {ssog}
        pos:  {self.pos}
        disk: {sdisk}
        """

class Game():
    """
    Game class
    """
    def __init__(self, dark_player_name, light_player_name):
        self.sog = create_sog()
        self.dark_player_name = dark_player_name
        self.light_player_name = light_player_name
        self.next_disk = types.Disk.DARK
    
    def put(self, pos, disk):
        if disk != self.next_disk:
            raise InvalidDiskColorError(disk)
        self.sog = calc_sog_after_put_disk(self.sog, pos, disk)
    
    def turn(self):
        if self.next_disk == types.Disk.DARK:
            self.next_disk = types.Disk.LIGHT
        else:
            self.next_disk = types.Disk.DARK
    
    def isAbleToPut(self):
        avail_poss = get_available_positions(self.sog, self.next_disk)
        return len(avail_poss) != 0

    def countDisks(self):
        ndark, nlight, _ = board.count_soss(self.sog)
        return ndark, nlight

def create_sog():
    """
    Create a new sog in the initial state.

    Returns:
        [[othero.core.SOS]]:
            The newly created sog in the initial state.
    """
    return sog.duplicate_sog(INIT_SOG)

def is_put_disk_valid(sog, pos, disk):
    """
    Check if putting the disk at the position is allowed by the
    osero rule.

    Args:
        sog [[othero.core.SOS]]:
            State of a game to be converted.

        pos (int, int):
            Position where <disk> is to be put.

            The int values represent row and collumn number
            respectively. They begin from 0.
        
        disk othero.core.Disk:
            The disk to be put. 
    
    Returns:
        bool:
            The validity of putting <disk>.
    """
    return forward.is_sos_change_valid(sog, pos, types.Disk.toSOS(disk))

def calc_sog_after_put_disk(sog, pos, disk):
    """
    Put <disk> at the <pos> and calculate the resulting sog according
    to the osero rule.
    
    Args: 
        sog [[othero.core.SOS]]:
            State of the game.
    
        pos (int, int):
            Position where <disk> is to be put.
    
            The int values represent row and collumn number
            respectively. They begin from 0.
    
        disk othero.core.Disk:
            The disk to be put.
    
    Returns:
        sog [[othero.core.SOS]]:
            Return the new state of the game after <disk> is put.
    
    Errors:
        othero.game.utils.InvalidDiskPositionError:
            Indicate that putting the disk at the position is not
            allowed by the osero rule. Usually, this is because no
            disk is reversed after putting the disk.
    """
    if not is_put_disk_valid(sog, pos, disk):
        raise InvalidDiskPositionError(sog, pos, disk)

    return forward.calc_sog_after_sos_changed(sog, pos, types.Disk.toSOS(disk))

def get_available_positions(sog, disk):
    """
    Return a list of positions in <sog> where putting <disk> is allowed.

    Args:
        sog [[othero.core.SOS]]:
            Sog to be searched in. 
        
        disk othero.core.Disk:
            Disk to be put.
    
    Returns:
        [(int, int)]:
            List of positions in <sog> where putting <disk> is allowed.
    """
    sos = types.Disk.toSOS(disk)

    blank_poss = board.get_positions_in_sos(sog, types.SOS.BLANK)
    return [pos for pos in blank_poss \
                if forward.is_sos_change_valid(sog, pos, sos)]
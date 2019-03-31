# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import enum

""" NOTE
Terms: 
    sog: state of a game
    sos: state of a square
    sid: state in a direction
"""

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

class SOS(enum.IntEnum):
    """
    State of squares(SOS)
    """
    DARK  =  1
    LIGHT = -1
    BLANK =  0

class Disk(enum.Enum):
    DARK  = enum.auto()
    LIGHT = enum.auto()

    @staticmethod
    def toSOS(disk):
        """
        Convert Disk into SOS.

        Args:
            disk othero.core.Disk:
                Disk to be converted.
        
        Returns:
            othero.core.SOS:
                Resulting SOS from <disk>.
        """
        if disk == Disk.DARK:
            return SOS.DARK 
        else:
            return SOS.LIGHT

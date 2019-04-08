# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libsog, libpos, libtypes

class SOG(libsog.SOG):
    def __init__(self, *args, **argv):
        # esp: evaluation of a square position
        def calc_esp(sog, pos):
            if pos is None:
                return None
            if not sog.isInside(pos):
                return None
            ndir = 0
            pos_pairs = [
                (
                    libpos.advance_pos(pos, libtypes.Direction.UP),
                    libpos.advance_pos(pos, libtypes.Direction.LOW)
                ),
                (
                    libpos.advance_pos(pos, libtypes.Direction.RIGHT),
                    libpos.advance_pos(pos, libtypes.Direction.LEFT)
                ),
                (
                    libpos.advance_pos(pos, libtypes.Direction.UP_R),
                    libpos.advance_pos(pos, libtypes.Direction.LOW_L)
                ),
                (
                    libpos.advance_pos(pos, libtypes.Direction.UP_L),
                    libpos.advance_pos(pos, libtypes.Direction.LOW_R)
                )
            ]
            for poss in pos_pairs:
                if not(sog.isInside(poss[0]) and sog.isInside(poss[1])):
                    ndir += 1
            return ndir

        super().__init__(*args, **argv)
        espss = [
            [calc_esp(self, pos) for pos in poss]
            for poss in self.getPosss()
        ]
        self.__espss = espss

    def getPosss(self):
        return [
            [(row, col) if self.isInside((row, col)) else None
                for col in range(len(self.__stencil[row]))]
            for row in range(len(self.__stencil))
        ]

    def getAllPositions(self):
        return [
            (row, col) for row in range(len(self.__stencil))
                       for col in range(len(self.__stencil[row]))
                       if self.isInside((row, col))
        ]

    def getEsp(self, pos):
        return self.__espss[pos[0]][pos[1]]

_STENCIL = [
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True]
]
_DARKS = [(1, 1), (2, 2)]
_LIGHTS = [(1, 2), (2, 1)]
_DEFAULT_SOG = SOG(_STENCIL, _DARKS, _LIGHTS)

def create_sog():
    """
    Return a new sog in the shape of 4x4. Some disks are already set.

    Returns:
        othero.core.libsog.SOG:
    
    """
    return _DEFAULT_SOG.duplicate()

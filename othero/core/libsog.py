# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes

""" NOTE
SOG:
    SOG is a two-dimentional array. The first dimention indicates a
    row, and the second indicates a collumn. For example, SOG[i][j]
    represents the sos in the intersection of i-th row and j-th collumn.
"""

from othero.core import libtypes

class SOG:
    def __init__(self, stencil, darks=[], lights=[]):
        self.__stencil = stencil
        self.__sosss = [
            [libtypes.SOS.BLANK if isInside else None for isInside in row]
            for row in stencil
        ]

        for pos in darks:
            self.setSos(pos, libtypes.SOS.DARK)
        for pos in lights:
            self.setSos(pos, libtypes.SOS.LIGHT)

    def __eq__(self, sog):
        return self.__sosss == sog.__sosss

    def duplicate(self):
        """
        Make a full copy (ie. deep copy).
        
        Return:
            othero.core.libsog.SOG:

        """
        new_sog = SOG(self.__stencil)
        new_sog.__sosss = [
            [sos for sos in row]
            for row in self.__sosss
        ]
        return new_sog

    def getSosss(self):
        return [[sos for sos in row] for row in self.__sosss]

    def getSos(self, pos):
        """
        Return a sos at <pos>.

        Args:
            pos (int, int):

        Returns:
            othero.core.libtypes.SOS:

        """
        return self.__sosss[pos[0]][pos[1]]

    def setSos(self, pos, sos):
        """
        Set a sos at <pos>.

        Args:
            pos (int, int):

            sos othero.core.libtypes.SOS:

        """
        if self.getSos(pos) is not None:
            self.__sosss[pos[0]][pos[1]] = sos

    def isInside(self, pos):
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
        if pos[0] not in range(len(self.__stencil)):
            return False

        row = self.__stencil[pos[0]]
        if pos[1] not in range(len(row)):
            return False

        return self.__stencil[pos[0]][pos[1]]

    def countSoss(self):
        """
        Count the number of each sos.
        
        Returns:
            int:
                The number of othero.core.libtypes.SOS.DARK in <sog>.

            int:
                The number of othero.core.libtypes.SOS.LIGHT in <sog>.

            int:
                The number of othero.core.libtypes.SOS.BLANK in <sog>.
        """
        ndark, nlight, nblank = 0, 0, 0
        for row in self.__sosss:
            for sos in row:
                if sos == libtypes.SOS.DARK:
                    ndark = ndark + 1
                elif sos == libtypes.SOS.LIGHT:
                    nlight = nlight + 1
                elif sos == libtypes.SOS.BLANK:
                    nblank = nblank + 1
        return ndark, nlight, nblank

    def getPositionsInSos(self, sos):
        """
        Return a list of positions where sos is <sos>.

        Args:
            sos othero.core.libtypes.SOS:
                Sos to be searched for.
        
        Returns:
            [(int, int)]:
                List of positions in <sog> where sos is <sos>.
        """
        poss = []
        for i in range(len(self.__sosss)):
            for j in range(len(self.__sosss[i])):
                if self.__sosss[i][j] == sos:
                    poss.append((i, j))
        return poss

    def toString(self):
        """
        Convert state of a game into string.

        This method is intended to be used to serialize state of a
        game so that it can be passed to another program.

        Args:
            sog othero.core.libsog.SOG:
                State of a game to be converted.
        
        Returns:
            string:
                Resulting string from <sog>.
        """
        soss = [sos for row in self.__sosss for sos in row if sos is not None]
        s = ""
        for sos in map(int, soss):
            s = s + "," + str(sos)
        return s[1:]

    def initFromString(self, s):
        """
        Initialize <sog> with <s>.

        This method is intended to be used to deserialize state of a
        game passed from another program so that it can be used inside
        of this program.

        Args:
            sog othero.core.libsog.SOG:
                Sog to be initialized.

            s string:
                String to be converted.
        """
        ps = list(map(int, s.split(',')))
        i = 0
        for row in range(len(self.__sosss)):
            for col in range(len(self.__sosss[row])):
                if self.__sosss[row][col] is None:
                    continue

                if i < len(ps):
                    self.__sosss[row][col] = ps[i]
                else:
                    self.__sosss[row][col] = None

                i += 1

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

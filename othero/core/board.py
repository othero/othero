# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import types

def count_soss(sog):
    """
    Count the number of each sos in the <sog>.

    Args:
        sog [[othero.core.SOS]]:
            State of the game.
    
    Returns:
        int:
            The number of othero.core.SOS.DARK in <sog>.

        int:
            The number of othero.core.SOS.LIGHT in <sog>.

        int:
            The number of othero.core.SOS.BLANK in <sog>.
    """
    ndark, nlight, nblank = 0, 0, 0
    for row in sog:
        for sos in row:
            if sos == types.SOS.DARK:
                ndark = ndark + 1
            elif sos == types.SOS.LIGHT:
                nlight = nlight + 1
            else:
                nblank = nblank + 1
    return ndark, nlight, nblank

def get_positions_in_sos(sog, sos):
    """
    Return a list of positions in <sog> where sos is <sos>.

    Args:
        sog [[othero.core.SOS]]:
            Sog to be searched in. 
        
        sos othero.core.SOS:
            Sos to be searched for.
    
    Returns:
        [(int, int)]:
            List of positions in <sog> where sos is <sos>.
    """
    poss = []
    for i in range(len(sog)):
        for j in range(len(sog[i])):
            if sog[i][j] == sos:
                poss.append((i, j))
    return poss

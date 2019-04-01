# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libsog, libpos
from othero.rule import utils

def is_sos_restore_valid(sog, pos):
    """
    Checks whether the sos restoration is allowed by osero rule.

    Args:
        sog [[othero.core.SOS]]:

        pos (int, int):
        
    Returns:
        bool:
            Validity of restoring sos at <pos>.
    """
    sos = sog[pos[0]][pos[1]]
    fv = any(map(bool, utils.calc_all_sids(sog, pos, sos).values())) 
    if fv:
        return False

    bv = any(map(bool, utils.calc_all_sidbs(sog, pos).values())) 
    return bv

def calc_sogs_after_sos_restored(sog, pos, sos):
    """
    Restore sos at the <pos> to <sos> and calculate the resulting
    possible sogs according to the osero rule.

    Args: 
        sog [[othero.core.SOS]]:

        pos (int, int):

        sos othero.core.SOS:
            Sos which the square is to be restored to.

    Returns:
        [[[othero.core.SOS]]]:
            A list of possible sogs after the sos restoration.
    """
    sidbs = utils.calc_all_sidbs(sog, pos)

    sog = libsog.duplicate_sog(sog)
    sog[pos[0]][pos[1]] = sos

    isogs, jsogs = [], [sog]
    for direction, sidb in sidbs.items():
        isogs, jsogs = jsogs, []
        # Update isogs.
        for isog in isogs:
            # The number of disks restored is from 0 to <sidb>.
            for ndisk in range(0, sidb+1):
                jsog = libsog.duplicate_sog(isog)
                jsogs.append(jsog)
                # Restore sog.
                for i in range(0, ndisk+1):
                    row, col = libpos.advance_pos(pos, direction, i)
                    jsog[row][col] = sos

    # The first sog is the same as sog before restoration, which is the
    # result of choosing no restoration for all the directions.
    return jsogs[1:]

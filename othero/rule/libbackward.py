# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libsog, libpos, libtypes
from othero.rule import utils
import itertools

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
    def changeSosInOneDirection(sog, pos, direction, sos, nsquare):
        for i in range(1, nsquare+1):
            row, col = libpos.advance_pos(pos, direction, i)
            sog[row][col] = sos

    def changeSosInAllDirections(sog, pos, sos, dn):
        for direction, nsquare in dn.items():
            changeSosInOneDirection(sog, pos, direction, sos, nsquare)

    sidbs = utils.calc_all_sidbs(sog, pos)

    sidbls = []
    dirkeys = []
    for key, sidb in sidbs.items():
        sidbls.append(sidb)
        dirkeys.append(key)

    ncmbs = [{d: n for d, n in zip(dirkeys, nls)}
             for nls in itertools.product(*map(
                 lambda sidb: range(sidb+1),
                 sidbls
             ))
             ][1:]

    prev_sos = sog[pos[0]][pos[1]]
    if prev_sos == libtypes.SOS.DARK:
        asos = libtypes.SOS.LIGHT
    elif prev_sos == libtypes.SOS.LIGHT:
        asos = libtypes.SOS.DARK

    sog = libsog.duplicate_sog(sog)
    sog[pos[0]][pos[1]] = sos

    prev_sogs = []
    for ncmb in ncmbs:
        prev_sog = libsog.duplicate_sog(sog)
        prev_sogs.append(prev_sog)
        changeSosInAllDirections(prev_sog, pos, asos, ncmb)

    return prev_sogs

# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes, libsog

def get_winner_disk(sog):
    """
    Return a disk of the winner. This function does not check if the
    game was over, and you should check it before calling this.

    Args:
        sog othero.core.libsog.SOG:
    """
    ndark, nlight, _ = sog.countSoss()
    if ndark > nlight:
        return libtypes.Disk.DARK
    elif ndark < nlight:
        return libtypes.Disk.LIGHT
    else:
        return None

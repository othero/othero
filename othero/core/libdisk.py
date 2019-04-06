# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes

def next_disk(disk):
    """
    Return the disk which will be put after the current <disk>.

    Passing is not taken into consideration.

    Args:
        disk othero.core.libtypes.Disk:
            The current disk.
    
    Returns:
        othero.core.libtypes.Disk:
            The disk to be put next.
    """
    if disk == libtypes.Disk.DARK:
        return libtypes.Disk.LIGHT
    else:
        return libtypes.Disk.DARK

def prev_disk(disk):
    """
    Return the disk which will be put before the current <disk>.

    Passing is not taken into consideration.

    Args:
        disk othero.core.libtypes.Disk:
            The current disk.
    
    Returns:
        othero.core.libtypes.Disk:
            The disk to have been put before.
    """
    if disk == libtypes.Disk.DARK:
        return libtypes.Disk.LIGHT
    else:
        return libtypes.Disk.DARK
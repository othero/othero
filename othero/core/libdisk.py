# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes

def next_disk(disk):
    if disk == libtypes.Disk.DARK:
        return libtypes.Disk.LIGHT
    else:
        return libtypes.Disk.DARK

def prev_disk(disk):
    if disk == libtypes.Disk.DARK:
        return libtypes.Disk.LIGHT
    else:
        return libtypes.Disk.DARK
# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes, libsog

def sosss_to_sog(sosss):
    darks, lights = [], []
    for row in range(len(sosss)):
        for col in range(len(sosss[row])):
            if sosss[row][col] == libtypes.SOS.DARK:
                darks.append((row, col))
            elif sosss[row][col] == libtypes.SOS.LIGHT:
                lights.append((row, col))
    stencil = [
        [sos is not None for sos in row]
        for row in sosss
    ]
    return libsog.SOG(stencil, darks, lights)

class Test1:
    SOSSS = [
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
    ]

    DARKS = [
        (0, 1), (0, 3),
        (1, 0),
        (2, 0),
        (3, 0), (3, 1), (3, 2)
    ]

    LIGHTS = [
        (0, 2),
        (1, 1),
        (2, 1)
    ]

    STENCIL = [
        [True , True , True , True ],
        [True , True , True , True ],
        [True , True , True , True ],
        [True , True , True , True ]
    ]

    SOG = libsog.SOG(STENCIL, DARKS, LIGHTS)

class Test2:
    SOSSS = [
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.DARK ],
        [libtypes.SOS.DARK , None              , None              , libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , None              , None              , libtypes.SOS.BLANK],
        [libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.DARK , libtypes.SOS.BLANK]
    ]

    DARKS = [
        (0, 1), (0, 3),
        (1, 0),
        (2, 0),
        (3, 0), (3, 1), (3, 2)
    ]

    LIGHTS = [
        (0, 2)
    ]

    STENCIL = [
        [True , True , True , True ],
        [True , False, False, True ],
        [True , False, False, True ],
        [True , True , True , True ]
    ]

    SOG = libsog.SOG(STENCIL, DARKS, LIGHTS)

class Test3:
    SOSSS = [
        [None              , None              , libtypes.SOS.BLANK, libtypes.SOS.BLANK, None              , None              ],
        [None              , libtypes.SOS.BLANK, libtypes.SOS.LIGHT, libtypes.SOS.DARK , libtypes.SOS.BLANK, None              ],
        [libtypes.SOS.BLANK, libtypes.SOS.DARK , None              , None              , libtypes.SOS.LIGHT, libtypes.SOS.BLANK],
        [libtypes.SOS.BLANK, libtypes.SOS.LIGHT, None              , None              , libtypes.SOS.DARK , libtypes.SOS.BLANK],
        [None              , libtypes.SOS.BLANK, libtypes.SOS.DARK , libtypes.SOS.LIGHT, libtypes.SOS.BLANK, None              ],
        [None              , None              , libtypes.SOS.BLANK, libtypes.SOS.BLANK, None              , None              ]
    ]

    SOG = sosss_to_sog(SOSSS)

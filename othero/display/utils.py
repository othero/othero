# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.core import libtypes

def visualize_sos(sos):
    """
    Convert sos to a visible symbol.
    
    The resulting symbols are:
    DARK : 'x'
    LIGHT: 'o'
    BLANK: ' '
    None : '-'

    Args:
        sos othero.core.libtypes.SOS:
            Sos to be converted.

    Returns:
        str:
            Resulting str from <sos>.            
    """
    if sos == libtypes.SOS.DARK:
        return 'x'
    elif sos == libtypes.SOS.LIGHT:
        return 'o'
    elif sos == libtypes.SOS.BLANK:
        return ' '
    else:
        return '-'

def visualize_sog(sog):
    """
    Convert sog to a two-dimentional list of the visible symbols.

    Args:
        sog othero.core.libsog.SOG:
            Sog to be converted.

    Returns:
        [[str]]:
            Resulting list from <sog>.
    """
    return [[visualize_sos(sos) for sos in row] for row in sog.getSosss()]

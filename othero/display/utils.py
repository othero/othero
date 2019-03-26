# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero import core

def visualize_sos(sos):
    """
    Convert othero.core.SOS to a visible symbol.
    
    The resulting symbols are:
    DARK : 'x'
    LIGHT: 'o'
    BLANK: ' '

    Args:
        sos othero.core.SOS:
            Sos to be converted.

    Returns:
        str:
            Resulting str from <sos>.            
    """
    if sos == core.SOS.DARK:
        return 'x'
    elif sos == core.SOS.LIGHT:
        return 'o'
    else:
        return ' '

def visualize_sog(sog):
    """
    Convert othero.core.SOG to a two-dimentional
    list of the visible symbols.

    Args:
        sog othero.core.SOG:
            Sog to be converted.

    Returns:
        [[str]]:
            Resulting list from <sos>.
    """
    return [[visualize_sos(sos) for sos in row] for row in sog]


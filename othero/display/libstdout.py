# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

from othero.display import utils

def display_sog_to_shell(sog):
    """
    Display othero.core.libtypes.SOG to the shell.

    Args:
        sog othero.core.libsog.SOG:
            Sog to display.

    Returns:
        [[str]]:
            Resulting list from <sos>.
    """
    class Shower:
        def __init__(self, row):
            self.__prev_vsos, self.__next_vsos = '', ''
            self.__irow = iter(row)

        def initShower(self):
            try:
                self.__prev_vsos, self.__next_vsos = self.__next_vsos, next(self.__irow)
                return True
            except StopIteration:
                return False

        def showNones(self):
            if self.__next_vsos != '-':
                return True

            while True:
                if self.__prev_vsos != '-' and self.__prev_vsos != '':
                    print("| ", end="")
                else:
                    print("  ", end="")
                try:
                    self.__prev_vsos, self.__next_vsos = self.__next_vsos, next(self.__irow)
                    if self.__next_vsos != '-':
                        return True
                except StopIteration:
                    return False

        def showSoss(self):
            if self.__next_vsos == '-':
                return True

            while True:
                print('|', end="")
                print(self.__next_vsos, end="")
                try:
                    self.__prev_vsos, self.__next_vsos = self.__next_vsos, next(self.__irow)
                    if self.__next_vsos == '-':
                        return True
                except StopIteration:
                    return False

        def finish(self):
            if self.__next_vsos == '':
                return
            elif self.__next_vsos == '-':
                print(' ', end="")
                return
            else:
                print('|', end="")
                return
        
    vsog = utils.visualize_sog(sog)

    for row in vsog:
        shower = Shower(row)
        if shower.initShower():
            while True:
                if not shower.showNones():
                    break
                if not shower.showSoss():
                    break
        shower.finish()
        print()
    print()

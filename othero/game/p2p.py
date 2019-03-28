# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

# p2p module includes a osero game in a scenario of person to person.

import re

from othero import core
from othero.display import stdout
from othero.game import utils

class InvalidPositionInputError(Exception):
    def __init__(self, spos):
        self.spos = spos
    
    def __str__(self):
        return f"spos: {self.spos}"

def p2p_game(dark_player_name, light_player_name):
    game = utils.Game(dark_player_name, light_player_name)
    finished = False
    while not finished:
        stdout.display_sog_to_shell(game.sog)
        while True:
            try: 
                pos = prompt(game)
                game.put(pos, game.next_disk)
            except (IndexError, utils.InvalidDiskPositionError):
                print("Putting the disk at this position is not allowed.")
                continue

            break
        game.turn()

        npass = 0
        NPLAYER = 2
        while not game.isAbleToPut():
            npass += 1
            if npass == NPLAYER:
                finished = True
                break
            game.turn()
    
    ndark, nlight = game.countDisks()
    if ndark > nlight:
        winner = "DARK"
    elif ndark < nlight:
        winner = "LIGHT"
    else:
        winner = ""
    
    stdout.display_sog_to_shell(game.sog)
    if winner != "":
        print(f"WINNER: {winner}")
    else:
        print("DRAW")
    
def prompt(game):
    if game.next_disk == core.Disk.DARK:
        sdisk = "DARK"
    else:
        sdisk = "LIGHT"

    while True:
        try:
            print(f"{sdisk}> ", end="")
            pos = parse(input())
            break
        except InvalidPositionInputError as err:
            print(f"Invalid input: {err.spos}")

    return pos

def parse(spos):
    matches = re.search(
            r"^" + r"\s*\(\s*"
          + r"(\d+)" + r"\s*,\s*" + r"(\d+)"
          + r"\s*\)\s*" + r"$",
          spos)
    if matches == None:
        raise InvalidPositionInputError(spos)

    srow, scol = matches.group(1), matches.group(2)
    row, col = int(srow), int(scol)
    return (row, col)

if __name__ == "__main__":
    p2p_game("alice", "bob")
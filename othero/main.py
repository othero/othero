# coding: utf-8

# Copyright (C) 2019 Tanaka Tatsuya and contributors
#
# This source code is licensed under the MIT License found in
# the LICENSE file in the root directory of this source tree.

import time

from othero.core import libtypes

from othero.core import libsog
from othero.search import libfws

def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(f"{stop-start} seconds")
    return wrapper

@stopwatch
def main():
    pass

if __name__ == "__main__":
    main()

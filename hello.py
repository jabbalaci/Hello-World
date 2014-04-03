#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys


def main(name):
    print("Hello, {name}!".format(name=name))

##############################################################################

if __name__ == "__main__":
    name = "World"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    main(name)

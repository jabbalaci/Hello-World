#!/usr/bin/env python

import sys
import re

def main(name):
    print "Hello, %s!" % name

if __name__ == "__main__":
    name = 'World'
    if len(sys.argv) > 1:
        name = sys.argv[1]
    main(name)

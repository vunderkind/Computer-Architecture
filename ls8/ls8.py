#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# print("This is the name of the program: ", sys.argv[0])
# print('ARGUMENTS: ', str(sys.argv))
cpu.load(sys.argv[1])
cpu.run()

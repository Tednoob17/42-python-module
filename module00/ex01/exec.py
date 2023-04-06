#!/usr/bin/python3
import sys
print(' '.join(arg[::-1].swapcase() for arg in sys.argv[:0:-1]))

#!/usr/bin/python3
import sys
argv = sys.argv[1:]
v = 1
if len(sys.argv) > 1:
	print("AssertionError: more than one argument are provided")
elif type(sys.argv[1]) != type(v):
	print("AssertionError: argument is not an integer")
elif argv % 2 == 0:
	print("I'm Even.")
elif argv % 2 == 1:
	print("I'm Odd.")
else :
	print("I'm Zero.")

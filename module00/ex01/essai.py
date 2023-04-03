#!/usr/bin/python3
import getpass
import sys
words = sys.argv[1:]
sentence = " ".join(words)
print("[%s] %s" % (getpass.getuser(), sentence))
# reverse and copy sys.argv
argv = reversed(sys.argv)
# extract the first element
arg = argv.pop()
# stop iterating when there's no more args to pop()
while len(argv) > 0:
	if arg in ('-f', '--foo'):
		print('seen foo!')
	elif arg in ('-b', '--bar'):
		print('seen bar!')
	elif arg in ('-a', '--with-arg'):
		arg = arg.pop()
		print('seen value: {}'.format(arg))
# get the next value
arg = argv.pop()

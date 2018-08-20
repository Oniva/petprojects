#! python 3
#  reverse.py - reverse a string

import sys

def reverse(string):
    newString = ""
    i = len(string) - 1
    while i >= 0:
        newString += string[i]
        i -= 1
    print(newString)


reverse(sys.argv[1])
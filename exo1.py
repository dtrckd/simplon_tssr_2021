#!/bin/python
import sys

args = sys.argv

if len(args) != 2:
    print("Usage: prog.py NUMBER")
    exit()

number = int(args[1])

if number % 2 == 0:
    print("even")
else:
    print("odd")



#!/bin/python
import sys

#
# Add a SEP at the end of each line
#

path = sys.argv[1]
sep = sys.argv[2] # RFTM

def alter_file(path, sep):
   f = open(path)
   content = f.read()
   f.close()
   content = content.split("\n") # "salut ca va" -> ["salut", "ca", "va]
   for i in range(len(content)):
       content[i] = content[i] + " " + sep

   content = '\n'.join(content)
   #content = (" "+sep+" ").join(content) # ["salut", "ca", "va] -> "salut {sep} ca {sep} va"
   dest = path + ".tmp"
   f = open(dest, "w")
   f.write(content)


alter_file(path, sep)

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def Find(pat, txt):
  match = re.search(pat, txt)
  if match:
    return True
  else:
    return False
	

def getspecialfiles(dir):

  specialfiles = []
  filenames = os.listdir(dir)
  for filename in filenames:
    if Find(r'__\w+__',filename):
	  path = os.path.join(dir,filename)
	  specialfiles.append(os.path.abspath(path))

  # print(specialfiles)
  return specialfiles
	


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
	
  print(args)

  # +++your code here+++
  # Call your functions
  specialfiles = getspecialfiles(args[0])
  
  if todir != '':
    if not os.path.exists(todir):
      os.mkdir(todir)
  
    for file in specialfiles:
      fname = os.path.basename(file)
      shutil.copy(file, os.path.join(todir, fname))
	  
  elif tozip != '':
    pass
  else:
    pass
  
  
  
if __name__ == "__main__":
  main()

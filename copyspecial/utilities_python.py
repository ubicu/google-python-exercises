
# Exercises from the Utilities lecture

import sys
import os

def List(dir):
  filenames = os.listdir(dir)
  print filenames

def main():
  
  args = sys.argv[1:]

  if not args:
    print 'usage: utilities_python.py directory_name'
    sys.exit(1)
	
  # Test code
  List(args[0])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
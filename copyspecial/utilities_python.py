
# Exercises from the Utilities lecture

import sys
import os

# os.path.exists()

def List(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir,filename)
    print path
    print os.path.abspath(path)

def main():
  
  args = sys.argv[1:]

  if not args:
    print 'usage: python utilities_python.py directory_name (e.g., python utilities_python.py .)'
    sys.exit(1)
	
  # Test code
  List(args[0])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
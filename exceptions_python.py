 # Exceptions example from lecture
 
import sys
 
def Cat(filename):
  try:
    with open(filename, 'r') as f:
      text = f.read()
      print('---'+filename)
      print(text)
  except IOError:
    print("IOError: "+filename +"\n")
 
def main():
  args = sys.argv[1:]
  for arg in args:
    Cat(arg)
 
 
 # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  
  with open(filename, 'r') as f:
    contents = f.read()
    m = re.findall(r'GET\s(\S+puzzle\S+)', contents)
    
    dicts = {}
    for mi in m:
      basename = os.path.basename(mi)
      if basename not in dicts:
        dicts[basename] = "http://code.google.com"+mi
		
    sortedItems = sorted(dicts.items())
    out = [sortedItem[1] for sortedItem in sortedItems]
    return out
    
	
    
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  
  i=0
  for img_url in img_urls:
    print("Retrieving image "+str(i)+" ...")
    urllib.urlretrieve(img_url,dest_dir+"/img"+str(i)+".jpg")
    #urllib.urlretrieve(img_url,dest_dir+"/im"+str(i))
    i=i+1
	
  # Write index.html file
  with open(dest_dir+"/index.html",'w') as f:
    #f.write("<verbatim>")
    #f.write("\n")
    f.write('<!DOCTYPE html>')
    f.write("\n")
    f.write("<html>")
    f.write("\n")
    f.write("<body>")
    f.write("\n")
    for i in range(len(img_urls)):
      #f.write("<img src=\""+dest_dir+"/img"+str(i)+".jpg\">")
      f.write("<img src=\""+"img"+str(i)+".jpg\">")
      #f.write("<img src=\""+"img"+str(i)+"\">")
    print("\n")
    f.write("\n")
    f.write("</body>")
    f.write("\n")
    f.write("</html>")
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()

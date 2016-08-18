# More exercises from Utilities lecture

import urllib

uf = urllib.urlopen('http://www.google.com')
# print(uf.read())

urllib.urlretrieve('http://www.google.com/intl/en_ALL/images/logo.gif','google.gif')
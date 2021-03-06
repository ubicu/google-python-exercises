# Regular expression exercises from Google Python class


import re

# Example 1
match = re.search('iig','called piiig')
print(match)
print(match.group())

# Example 2
match = re.search('igs','called piiig')
print(match)

def Find(pat, txt):
	match = re.search(pat, txt)
	if match:
		print(match.group())
	else:
		print('Not found')

# Example 3
Find('iig','called piiig')
Find('igs','called piiig')

# Additional notes
# .(dot) any char
# \w word char
# \d digit
# \s whitespace \S non-whitespace
# + 1 or more
# * 0 or more

# Example 4
Find('...g','called piiig')

# Example 5
Find('..gs','called piiig')

# Example 6
Find('..g','called piiig Another match xxxg')

# Example 7
Find('x..g','called piiig Another match xxxg')

# Example 8
Find('c\.call','c.called piiig Another match xxxg')

# Example 9
Find(r'c\.call','c.called piiig Another match xxxg')

# Example 10
Find(r':\w\w\w','blah :cat blah blah')

# Example 11
Find(r':\d\d\d','blah :cat :123 blah blah')

# Example 12
Find(r'\d\d\d','blah :cat :123 blah blah')

# Example 13
Find(r'\d\s+\d\s+\d','blah :cat :1    2     3 blah blah')

# Example 14
Find(r':\w+','blah :kitten :1    2     3 blah blah')

# Example 15
Find(r':.+','blah :kitten :1    2     3 blah blah')

# Example 16
Find(r':\w+','blah :kitten123%&fd*^ :1    2     3 blah blah')

# Example 17
Find(r':\S+','blah :kitten123%&fd*^ :1    2     3 blah blah')

# Example 18
Find(r'\w+@\w+','My email nick.p@gmail.com blah @')

# Example 19
Find(r'[\w.]+@[\w.]+','My email nick.p@gmail.com blah @') # Set of characters allowed, inside []

# Example 20
Find(r'[\w.]+@[\w.]+','My email .nick.p@gmail.com blah @') 

# Example 21
Find(r'\w[\w.]+@[\w.]+','My email .nick.p@gmail.com blah @') 

# Example 22 - Get the username and hostname
m = re.search(r'(\w[\w.]+)@([\w.]+)', 'My email .nick.p@gmail.com blah @')
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))

# Example 23
out = re.findall(r'\w[\w.]+@[\w.]+','My email .nick.p@gmail.com blah @ test@email.com')
print(out)

# Example 24
out = re.findall(r'(\w[\w.]+)@([\w.]+)','My email .nick.p@gmail.com blah @ test@email.com')
print(out)

# Example 25
out = re.findall(r'(\w[\w.]+)@([\w.]+)','My email .niCk.p@gmail.com blah @ test@email.com', re.IGNORECASE)
print(out)

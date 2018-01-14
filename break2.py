#!/usr/bin/python
# Filename: break.py
a=True
while a==True:
	s = raw_input('Enter something : ') 
	print 'Length of the string is', len(s)
	if s == 'quit':
		a=False
else:
	print 'Done'
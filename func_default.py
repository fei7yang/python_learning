#!/usr/bin/python
# Filename: func_default.py
def say(message, times = 1): #message赋值是无用的，只有末尾的参数可以有默认值
	print message * times
say('Hello') 
say('World', 5)
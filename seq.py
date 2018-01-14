#!/usr/bin/python #Filename: seq.py
shoplist = ['apple', 'mango', 'carrot', 'banana']
#Indexingor 'Subscription' operation 
print'Item0 is', shoplist[0] 
print'Item1 is', shoplist[1]
print'Item2 is', shoplist[2]
print'Item3 is', shoplist[3] 
print'Item-1 is', shoplist[-1] 
print'Item-2 is', shoplist[-2]
#Slicingon alist
print'Item1 to 3 is', shoplist[1:3]
print'Item2 to end is', shoplist[2:] 
print'Item1 to -1 is', shoplist[1:-1] 
print'Item start to end is', shoplist[:]
#Slicingon astring
name='swaroop'
print'characters1 to 3 is', name[1:3] 
print'characters2 to end is', name[2:] 
print'characters1 to -1 is', name[1:-1] 
print'characters start to end is', name[:]
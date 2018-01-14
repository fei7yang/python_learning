poem='''\
Programming is fun
WTF is this poem??????????????
'''

f=file('poem.txt','w')
f.write(poem)
f.close()

f=file('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,
f.close()

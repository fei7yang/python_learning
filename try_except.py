import sys

try:
    s=raw_input('Enter something --->')
except EOFError:
    print'Why did you do an EOF on me?'
    sys.exit()
except:
    print'Some error/exception occurred.'

print'Done'

import sys
try:
    while True:
        line1=sys.stdin.readline().strip()
        line2=sys.stdin.readline().strip()
        lines=line2.split(" ")
        if line1=="" or line2=="" or int(line1)!=int(len(lines)):
            break
        lines.sort(*,reverse=True)
        print lines
        for i in range(0,len(lines)-1):
            x=lines[i]
            for j in range(0,len(lines)-1):
                y=lines[j]
                pass
except:
    pass
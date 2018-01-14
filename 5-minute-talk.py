#coding=utf-8
import sys

line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
#print type(line1)
value1 = map(int, line1.split())
value2 = map(int, line2.split())
mini=value2[0]
s=value1[0]
x=value1[1]
#print mini
if(value1[0]==len(value2)):
    for i in range(s-1):
        if(value2[i]>value2[i+1]):
            mini=value2[i+1]
    #print mini

mini_p=value2.index(mini)

for j in range(value1[0]):
    value2[j]=value2[j]-mini
#print value2
value2[x-1]=value2[x-1]-1
#print value2
value2[mini_p]=s*1+1

for k in range(0,value2.__len__()):
    value2[k] = str(value2[k])
value3=" ".join(value2)
print value3
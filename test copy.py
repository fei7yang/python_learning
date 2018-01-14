#coding=utf-8
import os
import subprocess
from datetime import datetime


output = subprocess.check_output("cd /Users/dongl/.jenkins/workspace/ta-aws/;git diff HEAD~2", shell=True)
print output

 
str = '/Users/dongl/.jenkins/workspace/ta-aws/target/' + datetime.now().strftime("%Y%m%d_%H%M%S")  
#判断文件是否存在，若文件存在则继续，直到该文件夹下不包含该文件名
print str

while True==os.path.exists(str):
    str = str + datetime.now().strftime("%Y%m%d_%H%M%S")  
print str

f = open(str, 'w')
f.write(output)
f.close()
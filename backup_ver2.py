import os
import time

source=['/Users/dongl/Desktop/base']
#adding files here, for different dirs
target_dir='/Users/dongl/Desktop/'

today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')
print today
print now

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory',today

target=today+os.sep+now+'.zip'
#os.sep means / according to os-system
print os.sep
print target

zip_command="zip -r '%s' %s" %(target,' '.join(source))

if os.system(zip_command)==0:
	print'Successful backup to',target
else:
	print'Backup FAILED'
import os
import time

source=['/Users/dongl/Desktop/base', '/Users/dongl/Desktop/base2']
#adding files here, for different dirs
target_dir='/Users/dongl/Desktop/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
print target
print ' '.join(source)

zip_command="zip -r '%s' %s" %(target,' '.join(source))
#zip -r target source1 source2...
if os.system(zip_command)==0:
	print'Successful backup to',target
else:
	print'Backup FAILED'
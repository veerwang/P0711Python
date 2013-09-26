#! /usr/bin/python

import os
import shutil
import glob
import sys
import math
import urllib2
import zlib

#need install sh lib
# yum install sh
# pip install sh
from sh import ls,df

print "import test"

#print current path
print os.getcwd()

#os.mkdir(os.getcwd()+"/help")
#shutil.move('help','think')

print glob.glob('*.py')

print math.pi

#for line in urllib2.urlopen("http://baidu.com"):
#	print line

s = "www.eddysun.comdsdsdsdsdsdsdsdsdshdshdsd"
t = zlib.compress(s)
n = zlib.decompress(t)

print len(s)
print s
print len(t)
print t
print len(n)
print n

print "-----------------------------------"
print math.sin(math.pi/4)


print ls("-la")
print df("-h")



#exit program directory
sys.exit()

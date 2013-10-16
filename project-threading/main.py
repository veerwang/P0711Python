#! /usr/bin/python

import tarfile 
import threading
import time
import os
import sys

print "threading test"

olddir  = os.getcwd() 
tardir  = "/home/kevin/armworkcopy/"
objfile = "Ruby" 
desfile = "Ruby.tar.bz2"

class AnsyTar(threading.Thread):
	def __init__(self,olddir,indir,infile,outfile):
		threading.Thread.__init__(self)
		self.infile  = infile
		self.outfile = outfile
		self.indir   = indir
		self.olddir  = olddir
		self.flag    = "f" 
	def run(self):
		os.chdir(self.indir)
		IsExists = os.path.exists(self.infile)
		if not IsExists:
			print "error: file need to tar not found"
		else:
			tar = tarfile.open(self.outfile,'w|bz2')
			tar.add(self.infile);
			tar.close()
			os.chdir(self.olddir)
			self.flag = "t"
			print "tar job finished"

	def getflag(self):
		return self.flag

background = AnsyTar(olddir,
		     tardir,
		     objfile,
		     desfile)
background.start()

second = 0
print str(second) + "second ..."
while background.getflag() == 'f':
	time.sleep(1)
	second = second + 1
	print str(second) + "second ..."

background.join()

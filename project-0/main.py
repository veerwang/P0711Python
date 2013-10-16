#! /usr/bin/python

#program block 
import sys
from timeit import Timer

print __name__
print dir(sys)

print Timer('x = 1000 / 20','x=1').timeit()
print Timer('x = 1000 / 20','x=1').timeit()

x = 1000 / 20
print 'x = ' + str(x) 
print '5'.zfill(5)


print "{0} love {1}".format('kevin','lingjian')


a = 0
while a < 7:
	if a == 4:
		print a
	elif a == 5:
		print "nice"
	else:
		print "bad"

	a = a + 1

#do nothing just need stop
pass 

# >=0    <10
def debug(str):
	print str 

for i in range(0,10):   
	debug(i)

def Calculate_add(a,b):
	return lambda x: ( a + b ) * x

f = Calculate_add(10,9)

print f(2)

def Calculate_sub(a,b):
	return a - b

print Calculate_sub(99,8)

a=[1,2,3,4,5]


print a
for i in range(0,5):
	print a[i]

a.pop()
del a[2]
print a

class Baseclass:
	def __init__(self,id):
		self.m_ID = id
		print "create Baseclass"

	def __del__(self):
		print "destroy Baseclass"

	def ShowmeID(self):
		print self.m_ID

bs = Baseclass(20)
bs.ShowmeID()

class Drivedclass(Baseclass):
	def __del__(self):
		print "destroy Deviedclass"
	def __init__(self,id):
		self.m_ID = id
		print "create Driverclass"

ds = Drivedclass(21)
ds.ShowmeID()

dv = Baseclass(5)
dv.ShowmeID()

bs.ShowmeID()

# just declear class
class Baseclass:
	pass

#show the current path
import os
print os.getcwd()

import glob
print glob.glob("*.py")

import math
print math.cos(math.pi/4)
print math.pow(10,2)

print "---------------------"
temp = 2
print temp

del temp

temp = 5
print temp

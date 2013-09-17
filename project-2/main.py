#! /usr/bin/python

print "directory test"

d = {'x':42,'y':43,'z':44}

print d['x']
print d['y']
print d['z']

print d.items()
print d.keys()
print d.values()

d.clear()

a = [100,101,108,999,999]

print a[1]
print a.count(999)

f = open("test.txt","r")
while True:
	line = f.readline()
	if line:
		print line
	else:
		break;
f.close()

f = open("test.txt","r")
for line in f:
	print line
f.close()

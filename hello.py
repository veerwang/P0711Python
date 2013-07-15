#! /usr/bin/python

#import Tkinter

from Tkinter import *

def G_Show_Me(name):
	print name

class Base:
	name   = "kevin"
	myid   = 10

	@staticmethod
	def Prinf_ID(self):
		print self.myid

	def __init__(self):
		self.name = "none"

	def __del__(self):
		print "destroy Base class"

	def init_class(self,name):
		self.name = name

	def show_name(self):
		print self.name

print "hello the world"

d = 4

name = 'kevin'

for i in range(0,d):
	if i == 2:
		print name,"~",i
i = 0

while i<=5: 
	print i	
	i = i + 1

base = Base()
base.show_name()
base.init_class("veer")
base.show_name()
Base.Prinf_ID(base)

G_Show_Me("I am the Kind of world")

root = Tk()
root.geometry('400x300')
label = Label(root,text="hello the world")
label.pack()

root.mainloop()

#!  /usr/bin/env python
# -*- coding: utf-8 -*-

#	à traduire en Python
# cf /home/yves/2011/2014/automne/AEUG14/Sal12automne/backTicks.py
import commands

def laDate():
	dothis = "date"
	temp = commands.getoutput(dothis)
	return temp

if __name__ == '__main__':
	print laDate()

#!  /usr/bin/env python
# -*- coding: utf-8 -*-
#	date|awk '{print $2}'
#	à traduire en Python
# cf /home/yves/2011/2014/automne/AEUG14/Sal12automne/backTicks.py
import commands 
dothis = "ls *.py"
temp = commands.getoutput(dothis)  
print temp

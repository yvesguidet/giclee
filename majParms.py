#!  /usr/bin/env python
# -*- coding: utf-8 -*-

import ygGetDate
#	date|awk '{print $2}'
d = ygGetDate.laDate()
print "d = {}".format(d)

quantieme2Day = str.split(d)[1]
print "quantieme2Day = {}".format(quantieme2Day)
params = open('params.py', "a")
print "finir, écrire ds params.py"
print >>params, "quantieme2Day = {}".format(quantieme2Day)

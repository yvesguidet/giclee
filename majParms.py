#!  /usr/bin/env python
# -*- coding: utf-8 -*-

import ygGetDate
#	date|awk '{print $2}'
d = ygGetDate.laDate()
print "d = {}".format(d)

quantieme2Day = str.split(d)[1]
print "quantieme2Day = {}".format(quantieme2Day)
mois = str.split(d)[2]

nbJours = {'novembre': 30} # compléter ;)

print "nbJours = {}".format(nbJours)

print "mois = {}".format(mois)
nbJMois = nbJours[mois]

print "nbJMois = {}".format(nbJMois)

print "écriture de quantieme2Day = {} dans params.py".format(quantieme2Day)
print "écriture de nbJMois = {} dans params.py".format(nbJMois)
params = open('params.py', "a")
print "finir"
print >>params, "quantieme2Day = {}".format(quantieme2Day)
print >>params, "nbJMois = {}".format(nbJMois)

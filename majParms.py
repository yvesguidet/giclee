#!  /usr/bin/env python
# -*- coding: utf-8 -*-
from sys import path
path.append('/home/yves/2011/2016/automne/rentree/pymmPremCrochet')
from FinProvisoire import FinProvisoire
import ygGetDate
#	date|awk '{print $2}'
d = ygGetDate.laDate()
print "d = {}".format(d)

quantieme2Day = str.split(d)[1]
print "quantieme2Day = {}".format(quantieme2Day)
mois = str.split(d)[2]

nbJours = {'novembre': 30, 'décembre' : 31} # compléter ;)

print "nbJours = {}".format(nbJours)

from semCour import semCour

semCour = semCour()

print "semCour = {}".format(semCour)
print "type(semCour) = {}".format(type(semCour))

semCour = int(semCour)

print "semCour = {}".format(semCour)
print "type(semCour) = {}".format(type(semCour))

semCour += 1

print "mois = {}".format(mois)
nbJMois = nbJours[mois]

print "nbJMois = {}".format(nbJMois)

print "écriture de quantieme2Day = {} dans params.py".format(quantieme2Day)
print "écriture de nbJMois = {} dans params.py".format(nbJMois)
params = open('params.py', "a")
print "finir"
print >>params, "sem = '{}'".format(semCour)
print >>params, "quantieme2Day = {}".format(quantieme2Day)
print >>params, "nbJMois = {}".format(nbJMois)
quantiemeDuLundi = int(quantieme2Day) + 1 # grosse triche
print >>params, "quantiemeDuLundi = {}".format(quantiemeDuLundi)

print "Et voilou"

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

nbJours = {	'novembre': 30,
			'décembre' : 31,
			'janvier' : 31,
			'février' : 28, # patch prévu pour 2020 ^^
			'mars' : 31,
			'avril' : 30,
			'mai' : 31}	# compléter ;)

print "nbJours = {}".format(nbJours)

path.append('/home/yves/2011/2017/printemps/dev/Python/outils/giclee/semCour')
from semCour import semCour

semCour = semCour()

print "semCour = {}".format(semCour)
print "type(semCour) = {}".format(type(semCour))

print "semCour = {}".format(semCour)
print "type(semCour) = {}".format(type(semCour))

semCour = semCour[3:]
print "après nettoyage début : semCour = {}".format(semCour)

semCour = semCour[:2]
print "après nettoyage fin : semCour = {}".format(semCour)

# dimanche 28 mai 2017, 09:04:03 (UTC+0200)
semCour = int(semCour)

# semCour += 1

# dimanche 1 janvier 2017, 09:45:32 (UTC+0100)
if semCour == 53:
	semCour = 1

print "mois = {}".format(mois)
nbJMois = nbJours[mois]

print "nbJMois = {}".format(nbJMois)

print "écriture de quantieme2Day = {} dans params.py".format(quantieme2Day)
print "écriture de nbJMois = {} dans params.py".format(nbJMois)
# samedi 11 mars 2017, 09:31:20 (UTC+0100)
params = open('/home/yves/2011/2017/printemps/dev/Python/outils/giclee/params.py', "w")


path.append('/home/yves/2011/2017/printemps/dev/Python/outils/giclee/jourSem')
from jourSem import jourSem, nbJoursDIciLundi

jourS = jourSem()
print "jourS = {}".format(jourS)
#	assert(jourS == 'dim')

quantiemeDuLundi = int(quantieme2Day) + nbJoursDIciLundi() # samedi 25 février 2017, 07:04:06 (UTC+0100)
print >>params, "quantiemeDuLundi = {}".format(quantiemeDuLundi)
#	print "finir"
print >>params, "sem = '{}'".format(semCour)
print >>params, "quantieme2Day = {}".format(quantieme2Day)
print >>params, "nbJMois = {}".format(nbJMois)

params.close()
print "Et voilou"

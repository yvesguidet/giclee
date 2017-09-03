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
			'mai' : 31,
			'juin' : 30,
			'juillet' : 31,
			'août' : 31,
			'septembre' : 30}	# compléter ;)

print "nbJours = {}".format(nbJours)

# mardi 25 juillet 2017, 08:28:50 (UTC+0200)
path.append('/home/yves/2011/dev/Python/outils/semCour')
from semCour import semCour

semCour = semCour()

print "semCour = {}".format(semCour)

semCour = semCour[3:]
print "après nettoyage début : semCour = {}".format(semCour)

semCour = semCour[:2]
print "après nettoyage fin : semCour = {}".format(semCour)

# dimanche 28 mai 2017, 09:04:03 (UTC+0200)
semCour = int(semCour)

# dimanche 23 juillet 2017, 10:56:53 (UTC+0200)
# 	non !

# semCour += 1	# oui ou non ?

# dimanche 1 janvier 2017, 09:45:32 (UTC+0100)
if semCour == 53:
	semCour = 1

print "mois = {}".format(mois)
nbJMois = nbJours[mois]

print "nbJMois = {}".format(nbJMois)

print "écriture de quantieme2Day = {} dans params.py".format(quantieme2Day)
print "écriture de nbJMois = {} dans params.py".format(nbJMois)
# samedi 11 mars 2017, 09:31:20 (UTC+0100)
#	params = open('/home/yves/2011/2017/printemps/dev/Python/outils/giclee/params.py', "w")

# dimanche 9 juillet 2017, 10:11:06 (UTC+0200)
params = open('/home/yves/2011/dev/Python/outils/giclee/params.py', "w")


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

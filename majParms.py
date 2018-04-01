#!  /usr/bin/env python
# -*- coding: utf-8 -*-

bavard = True

from sys import path
import ygGetDate
#	date|awk '{print $2}'

import time

import locale

locale.setlocale(locale.LC_ALL, ('fr', 'utf-8'))

def majParms():
	ati = time.asctime()

	quantieme2Day = str.split(ati)[2]

	mois = str.split(ati)[1]

	#	assert mois == 'Mar'
	moisFrancais = {'Mar' : 'mars',
					'Apr' : 'avril'}
	mois = moisFrancais[mois]

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
				'septembre' : 30,
				'octobre' : 31,
				'novembre' : 30}	# compléter ;)

	# mardi 25 juillet 2017, 08:28:50 (UTC+0200)
	#	path.append('/home/yves/2011/dev/Python/outils/semCour')
	#	from semCour import semCour

	import datetime

	semCour = datetime.date.today().isocalendar()[1]
	if bavard:
		assert 0

	# dimanche 12 novembre 2017, 11:06:37 (UTC+0100)

	# dimanche 28 mai 2017, 09:04:03 (UTC+0200)
	#	semCour = int(semCour)

	# dimanche 23 juillet 2017, 10:56:53 (UTC+0200)
	# 	non !

	# vendredi 6 octobre 2017, 10:14:52 (UTC+0200)
	#	si ?
	# dimanche 15 octobre 2017, 09:46:35 (UTC+0200)
	# 	non !
	# provi
	#	jeudi 19 octobre 2017, 10:30:15 (UTC+0200)
	semCour += 1	# oui ou non ?

	# dimanche 1 janvier 2017, 09:45:32 (UTC+0100)
	if semCour == 53:
		semCour = 1

	nbJMois = nbJours[mois]

	# samedi 11 mars 2017, 09:31:20 (UTC+0100)
	#	params = open('/home/yves/2011/2017/printemps/dev/Python/outils/giclee/params.py', "w")

	# dimanche 9 juillet 2017, 10:11:06 (UTC+0200)
	params = open('/home/yves/2011/dev/Python/outils/giclee/params.py', "w")


	path.append('/home/yves/2011/dev/Python/outils/jourSem')
	from jourSem import jourSem, nbJoursDIciLundi

	jourS = jourSem()

	quantiemeDuLundi = int(quantieme2Day) + nbJoursDIciLundi() # samedi 25 février 2017, 07:04:06 (UTC+0100)

	# dimanche 31 décembre 2017, 08:37:48 (UTC+0100)
	if quantiemeDuLundi == 32:
		quantiemeDuLundi = 1	# affreux
	#	assert(quantiemeDuLundi <= 31)

	if semCour == 14:	# horrible patch
		quantiemeDuLundi = 26
		print  "quantiemeDuLundi = {}".format(quantiemeDuLundi)
		semCour -= 1
		print  "sem = '{}'".format(semCour)
		print  "quantieme2Day = {}".format(quantieme2Day)
		print  "type(quantieme2Day) = {}".format(type(quantieme2Day))
		quantieme2Day = '25'
		print  "nbJMois = {}".format(nbJMois)

	print >>params, "quantiemeDuLundi = {}".format(quantiemeDuLundi)
	print >>params, "sem = '{}'".format(semCour)
	print >>params, "quantieme2Day = {}".format(quantieme2Day)
	print >>params, "nbJMois = {}".format(nbJMois)

	params.close()

if  __name__ == '__main__':
	assert 0, 'later'
else:
	majParms()

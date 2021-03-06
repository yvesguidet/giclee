#!  /usr/bin/env python
# -*- coding: utf-8 -*-
from sys import path
import ygGetDate
#	date|awk '{print $2}'

import time

import locale

locale.setlocale(locale.LC_ALL, ('fr', 'utf-8'))

def majParms():
	ati = time.asctime()
	#	assert 0, 'majParms : ati = {}'.format(ati)

	quantieme2Day = str.split(ati)[2]

	mois = str.split(ati)[1]

	#	assert mois == 'May'
	moisFrancais = {'Mar' : 'mars',
					'Apr' : 'avril',
					'May' : 'mai',
					'Jun' : 'juin',
					'Jul' : 'juillet',
					'Aug' : 'août',
					'Sep' : 'septembre',
					'Oct' : 'octobre',
					'Nov' : 'novembre'}
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


	from sys import path

	d = datetime.date.today()	# auj
	# jour numérique
	jn = d.isocalendar()[2]
	print 'ls : jn = {}'.format(jn)
	# jour symbolique
	jourS = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim'][jn - 1]

	print 'jourS = {}'.format(jourS)

	from sys import path
	path.append('/home/yves/2011/2018/automne/cartes/giclee/XNextWeek/giclee/lundis')
	
	from ls import ls

	import datetime

	d = datetime.date.today()	# auj

	lundi = ls(d)
	print 'postTraitCHebdo.py : lundi = {}'.format(lundi)

	print 'postTraitCHebdo.py : d = {}'.format(d)

	quantiemeDuLundi = int(str(lundi).split('-')[2])
	print 'postTraitCHebdo.py : quantiemeDuLundi = {}'.format(quantiemeDuLundi)

	print  "nbJMois = {}".format(nbJMois)
	print  "quantiemeDuLundi = {}".format(quantiemeDuLundi)

	if quantiemeDuLundi > nbJMois:
		quantiemeDuLundi -= nbJMois

	# dimanche 31 décembre 2017, 08:37:48 (UTC+0100)
	if quantiemeDuLundi == 32:
		quantiemeDuLundi = 1	# affreux

	print >>params, "quantiemeDuLundi = {}".format(quantiemeDuLundi)
	print >>params, "sem = '{}'".format(semCour)
	print >>params, "quantieme2Day = {}".format(quantieme2Day)
	print >>params, "nbJMois = {}".format(nbJMois)

	params.close()

if  __name__ == '__main__':
	#	assert 0, 'later'
	majParms()
else:
	majParms()

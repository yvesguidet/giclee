#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias n='newMap.pl'

debourre = True # prévoir option -d

from insWeek import jours

# à passer en arg

import os

import majParms
majParms.majParms()

from sys import path
path.append('giclee')

import params

oct = '_'	# mieux que '-' pour modif
# lundi 16 octobre 2017, 09:45:42 (UTC+0200)

dirtest = 'essai'

import shutil
shutil.rmtree('essai', ignore_errors=True)

os.mkdir(dirtest)

# on se déplace sur le répertoire essai
# vendredi 20 octobre 2017, 09:11:55 (UTC+0200)
# après avoir planqué le répertoire courant

ici= os.getcwd()
os.chdir(dirtest)

from insWeek import insWeek, insVeille, insLend, majLienDsSuiv, numSemCour

for (increment, jour3lettres) in enumerate (jours):
	if debourre:
		#	print 'blouk : increment = {}'.format(increment)
		#	print 'blouk : jour3lettres = {}'.format(jour3lettres)

	#	util. str.format()
	#	mettre un format
		pass

	from sys import path

	path.append('/home/yves/2011/dev/Python/outils/jourSem')
	from jourSem import jourSem, nbJoursDIciLundi
	import time
	ati = time.asctime()

	quantieme2Day = str.split(ati)[2]

	path.append('/home/yves/2011/2018/automne/cartes/giclee/XNextWeek/giclee/lundis')
	from ls import ls

	import datetime

	d = datetime.date.today()	# auj

	lundi = ls(d)

	print 'giclee.py : d = {}'.format(d)

	quantiemeDuLundi = str(lundi).split('-')[2]
	print 'giclee.py : quantiemeDuLundi = {}'.format(quantiemeDuLundi)

	assert 0, 'OK ?'

	quantiemeDuLundi = int(quantieme2Day) + nbJoursDIciLundi() # samedi 25 février 2017, 07:04:06 (UTC+0100)

	nbJMois = params.nbJMois

	if quantiemeDuLundi > nbJMois:
		quantiemeDuLundi -= nbJMois

	# carteACreer = str(increment + quantiemeDuLundi) + '_sem' + params.sem

	quantieme = increment + quantiemeDuLundi
	if quantieme > 31:	# juillet
		quantieme -= 31

		print 'quantieme = {}'.format(quantieme)

	#	carteACreer = "{}{}_sem{}".format(jour3lettres, increment + quantiemeDuLundi, params.sem)
	carteACreer = "{}{}_sem{}".format(jour3lettres, quantieme, params.sem)
	print 'blouk : carteACreer = {}'.format(carteACreer)

	if jour3lettres != 'lun' and debourre:
		print 'giclee : increment = {}'.format(increment)

	if params.quantiemeDuLundi > params.nbJMois:
		params.quantiemeDuLundi = 1
	from sys import path
	path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/giclee/pyNewMap')
	import newMap

	carteACreer += '.mm'

	d1 = '/home/yves/2011/dev/Python/XCartes/XNextWeek/essais/'

	majLienDsSuiv(carteACreer, d1)

	newMap.main(nombase = carteACreer, leDir = os.getcwd(), dater = False, over = False)

	insWeek(carteACreer, os.getcwd())
	insVeille(carteACreer, os.getcwd())

#	on rejoue le match ^^

for (increment, jour3lettres) in enumerate (jours):
	#	print 'replay : increment = {}'.format(increment)
	#	print 'replay : jour3lettres = {}'.format(jour3lettres)

	#	majLienDsSuiv(carteACreer, d1, jour3lettres)

	from glob import glob

	ll = glob(jour3lettres + '*.mm')
	assert len(ll) == 1

	insLend(ll[0], os.getcwd())

# on revient
os.chdir(ici)


k = './try.sh'
os.system(k)

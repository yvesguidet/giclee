#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias n='newMap.pl'

debourre = True # prévoir option -d

from insWeek import jours

# à passer en arg

import os

#	import majParms
#	majParms.majParms()

from sys import path
path.append('giclee')

#	import params

oct = '_'	# mieux que '-' pour modif
# lundi 16 octobre 2017, 09:45:42 (UTC+0200)

dirtest = 'essai'

import shutil
#	shutil.rmtree('essai', ignore_errors=True)

# on se déplace sur le répertoire essai
# vendredi 20 octobre 2017, 09:11:55 (UTC+0200)
# après avoir planqué le répertoire courant

ici= os.getcwd()
os.chdir(dirtest)

from insWeek import insWeek, insVeille, insLend, majLienDsSuiv

for (increment, jour3lettres) in enumerate (jours):
	if debourre:
		#	print 'blouk : increment = {}'.format(increment)
		#	print 'blouk : jour3lettres = {}'.format(jour3lettres)

	#	util. str.format()
	#	mettre un format
		pass

	from sys import path

	import time
	ati = time.asctime()

	quantieme2Day = str.split(ati)[2]

	path.append('/home/yves/2011/2018/automne/cartes/giclee/XNextWeek/giclee/lundis')
	#	from ls import ls

	import datetime

	d = datetime.date.today()	# auj
#
	from semaineSuivante import lundiProchain

	#	lundi = ls(d)
	lundi = lundiProchain()

	if False:
		print 'giclee.py : lundi = {}'.format(lundi)
	m = int(str(lundi).split('-')[1])
	if False:
		print 'giclee.py : m = {}'.format(m)

	import lundis

	nbJMois = lundis.nbJMois(m)
	if False:
		print 'giclee.py : nbJMois = {}'.format(nbJMois)

	quantiemeDuLundi = int(str(lundi).split('-')[2])
	if False:
		print 'giclee.py : quantiemeDuLundi = {}'.format(quantiemeDuLundi)

	if False:
		print 'giclee.py : nbJMois = {}'.format(nbJMois)

	#	assert 0
	if quantiemeDuLundi > nbJMois:
		quantiemeDuLundi -= nbJMois

	quantieme = increment + quantiemeDuLundi
	if quantieme > 31:	# juillet
		quantieme -= 31

		if False:
			print 'quantieme = {}'.format(quantieme)

	from bugGicl import dirCartes, carteHebdo, numSemCour

	sem = numSemCour() + 1	#	naaaaaaaaaaaaaaaaan
	bl19 = lundiProchain()
	bl19 = numSemCour(bl19)

	bl19 = carteHebdo(bl19)

	print 'giclee.py : bl19 = {}'.format(bl19)

	if sem == 53:
		sem = 1

	if True:
		print 'giclee.py : sem = {}'.format(sem)

	carteACreer = "{}{}_sem{:02}".format(jour3lettres, quantieme, sem)

	if True:
		print 'blouk : carteACreer = {}'.format(carteACreer)
	#	assert 0, 'finir'

	if jour3lettres != 'lun' and debourre:
		if False:
			print 'blouk : increment = {}'.format(increment)

	quantiemeDuLundi = datetime.date.today()	# auj
	dd = d
	
#	/media/home/yves/2011/dev/Python/outils/giclee/semaineSuivante.py
#	def dem1(d = datetime.date.today()):
#	def lundiDernier():
#	def lundiProchain():
	
	d = lundiProchain()
	print 'blouk : (d, type(d)) = {}'.format((d, type(d)))
	d = int(str(d).split('-')[2])	# quantième lundi proch.
	
	if True:
		print 'd = {}'.format(d)
	if True:
		print 'type(d) = {}'.format(type(d))

	assert isinstance(d, int)
	
	m = int(str(dd).split('-')[1])	# le mois (de 1 à 12)
	if True:
		print 'm = {}'.format(m)
	if True:
		print 'type(m) = {}'.format(type(m))

	from njm import njm

	nbJMois = njm(m)
	if False:
		print 'nbJMois = {}'.format(nbJMois)

	if d > nbJMois:
		d = 1
	from sys import path
	path.append('/home/yves/2011/dev/Python/outils/pyNewMap')
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

	print 'giclee.py : ll = {}'.format(ll)

	##
#	def veille(c, d):
	from insWeek import veille


	i = jours.index(jour3lettres)
	if i == 0:
		continue
	
	assert len(ll) == 1

	insLend(ll[0], os.getcwd())

# on revient
os.chdir(ici)


k = './try.sh'
os.system(k)

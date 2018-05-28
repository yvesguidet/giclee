#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias n='newMap.pl'

debourre = False # prévoir option -d

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

# à passer en arg

import os

import majParms
majParms.majParms()

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

for (increment, jour3lettres) in enumerate (l):
	if debourre:
		print 'blouk : increment = {}'.format(increment)
		print 'blouk : jour3lettres = {}'.format(jour3lettres)

	#	util. str.format()
	#	mettre un format

	from sys import path

	path.append('/home/yves/2011/dev/Python/outils/jourSem')
	from jourSem import jourSem, nbJoursDIciLundi
	import time
	ati = time.asctime()

	quantieme2Day = str.split(ati)[2]
	quantiemeDuLundi = int(quantieme2Day) + nbJoursDIciLundi() # samedi 25 février 2017, 07:04:06 (UTC+0100)

	nbJMois = params.nbJMois
	if debourre:
		#	print 'blouk : increment = {}'.format(increment)
		print 'blouk : quantiemeDuLundi = {}'.format(quantiemeDuLundi)
		#	print 'blouk : type(increment) = {}'.format(type(increment))
		#	print 'blouk : jour3lettres = {}'.format(jour3lettres)
		print 'blouk : nbJMois = {}'.format(nbJMois)
		#	print 'blouk : params.sem = {}'.format(params.sem)
	if quantiemeDuLundi > nbJMois:
		quantiemeDuLundi -= nbJMois

	# carteACreer = str(increment + quantiemeDuLundi) + '_sem' + params.sem
	carteACreer = "{}{}_sem{}".format(jour3lettres, increment + quantiemeDuLundi, params.sem)
	#	print 'blouk : carteACreer = {}'.format(carteACreer)

	if jour3lettres != 'lun' and debourre:
		print 'giclee : increment = {}'.format(increment)
		#	assert 0, 'giclee.py : carteACreer = {}'.format(carteACreer)

	if params.quantiemeDuLundi > params.nbJMois:
		params.quantiemeDuLundi = 1
	from sys import path
	path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/giclee/pyNewMap')
	import newMap

	newMap.main(nombase = carteACreer, leDir = os.getcwd(), dater = False, over = False)

# on revient
os.chdir(ici)

k = './try.sh'
os.system(k)

#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

# à passer en arg

import os

k = './majParms.py'
print k
os.system(k)

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

for j in l:
	#	util. str.format()
	#	mettre un format
	carteACreer = j + str(params.quantiemeDuLundi) + '_sem' + params.sem

	k = 'newMap.py ' + carteACreer
	params.quantiemeDuLundi += 1
	if params.quantiemeDuLundi > params.nbJMois:
		params.quantiemeDuLundi = 1
	print k
	from sys import path
	path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/giclee/pyNewMap')
	import newMap

	newMap.main(nombase = carteACreer, leDir = os.getcwd(), dater = False, over = False)

# on revient
os.chdir(ici)

k = './try.sh'
print k
os.system(k)

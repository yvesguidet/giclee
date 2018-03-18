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

k = 'rm -rf {}'.format(dirtest)
print k

import shutil
shutil.rmtree('essai', ignore_errors=True)

os.mkdir(dirtest)
assert 0, 'good?'

# on se déplace sur le répertoire essai
# vendredi 20 octobre 2017, 09:11:55 (UTC+0200)
# après avoir planqué le répertoire courant

ici= os.getcwd()
os.chdir(dirtest)

for j in l:
	#	util. str.format()
	#	mettre un format
	k = 'newMap.py ' + j + str(params.quantiemeDuLundi) + '_sem' + params.sem
	params.quantiemeDuLundi += 1
	if params.quantiemeDuLundi > params.nbJMois:
		params.quantiemeDuLundi = 1
	print k
	os.system(k)

# on revient
os.chdir(ici)

k = './try.sh'
print k
os.system(k)

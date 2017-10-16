#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

# à passer en arg
from params import *

oct = '_'	# mieux que '-' pour modif

import os
# lundi 16 octobre 2017, 09:45:42 (UTC+0200)

dirtest = 'essai'

k = 'mkdir -p {}'.format(dirtest)
print k
os.system(k)
os.chdir(dirtest)

for j in l:
	#	util. str.format()
	#	mettre un format
	k = 'newMap.pl ' + j + str(quantiemeDuLundi) + '_sem' + sem
	quantiemeDuLundi += 1
	if quantiemeDuLundi > nbJMois:
		quantiemeDuLundi = 1
	print k
	os.system(k)

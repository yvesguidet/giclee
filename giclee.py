#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

# à passer en arg

sem = '26'
quantiemeDuLundi = 27
nbJMois = 30

sep = '_'	# mieux que '-' pour modif

import os

for j in l:
	#	util. str.format()
	#	mettre un format
	k = 'newMap.pl ' + j + str(quantiemeDuLundi) + '_sem' + sem
	quantiemeDuLundi += 1
	if quantiemeDuLundi > nbJMois:
		quantiemeDuLundi = 1
	print k
	os.system(k)

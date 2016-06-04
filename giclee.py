#!  /usr/bin/env python
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')
sem = '23'
quantieme = 6
sep = '_'	# mieux que '-' pour modif

import os

for j in l:
	#	util. str.format()
	#	mettre un format
	k = 'newMap.pl ' + j + str(quantieme) + '_sem' + sem
	quantieme += 1
	if quantieme > 31:
		quantieme = 1
	print k
	os.system(k)

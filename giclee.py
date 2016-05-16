#!  /usr/bin/env python
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')
sem = '20'
quantieme = 16
sep = '_'	# mieux que '-' pour modif

for j in l:
	#	util. str.format()
	#	mettre un format
	k = 'newMap.pl ' + j + str(quantieme) + '_sem' + sem
	quantieme += 1
	print k

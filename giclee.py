#!  /usr/bin/env python
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu')
sem = '19'
i = 9
sep = '_'	# mieux que '-' pour modif

for j in l:
	#	util. str.format()
	k = 'newMap.pl ' + j + str(i) + '_' + sem
	print k

#!  /usr/bin/env python
# alias n='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu')
sem = '19'
i = 9

for j in l:
	#	util. str.format()
	k = 'newMap.pl ' + j + str(i) + '-' + sem
	print k

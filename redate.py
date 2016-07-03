#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias finNomfic='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

from params import *


sep = '_'	# mieux que '-' pour modif

import os

# os.chdir('cartes')

from glob import glob

fics = glob('*sem' + sem + '*mm') # dimanche 19 juin 2016, 09:24:11 (UTC+0200)

print fics

for f in fics:
	finNomfic = f[3:]	# enlève 'lun', 'mar' ...
	#	print "finNomfic = {}".format(finNomfic)
	indiceBsoul = finNomfic.find('_')
	#	print "indiceBsoul = {}".format(indiceBsoul)
	quantiemeDuLundi = finNomfic[:indiceBsoul]
	#	print "quantiemeDuLundi = {}".format(quantiemeDuLundi)
	k = "modident {} {} {}".format(quantieme2Day, quantiemeDuLundi, f) # dimanche 19 juin 2016, 09:32:55 (UTC+0200)
	print k
	os.system(k)

#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# alias finNomfic='newMap.pl'

l = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

sem = '24'
quantieme = 16
zap = 12


sep = '_'	# mieux que '-' pour modif

import os

# os.chdir('cartes')

from glob import glob

fics = glob('*sem24*mm') # ne pas laisser en dur !!!

print fics

for f in fics:
	jour3car = f[0:3]
	print jour3car
	k = "modident {} {} {}".format("samedi", jour3car, f)
	#	print k

for f in fics:
	finNomfic = f[3:]	# enlève 'lun', 'mar' ...
	#	print "finNomfic = {}".format(finNomfic)
	indiceBsoul = finNomfic.find('_')
	#	print "indiceBsoul = {}".format(indiceBsoul)
	quantieme = finNomfic[:indiceBsoul]
	#	print "quantieme = {}".format(quantieme)
	k = "modident {} {} {}".format(zap, quantieme, f)# ne pas laisser "zap" en dur ;)
	print k
	os.system(k)

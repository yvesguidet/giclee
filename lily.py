# -*- coding: utf-8 -*-

from lxml import etree

import os

def lily(c, d):
	''' insère semaine, veille et lendemain'''

	print 'lily : c = {}'.format(c)
	print 'lily : d = {}'.format(d)

	nomLong = os.path.join(d, c)

	carte = etree.parse(nomLong)[0]

#	print(map.tag)

	carte.append( etree.Element("node") )

	print(etree.tostring(carte, pretty_print=True))

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py
#	def sauveCarte(a, f):
	assert 0, 'terminer'

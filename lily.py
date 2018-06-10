# -*- coding: utf-8 -*-

from lxml import etree

def lily(c, d):
	''' insère samaine, veille et lendemain'''

	print 'lily : c = {}'.format(c)
	print 'lily : d = {}'.format(d)

	carte = etree.Element("map")

#	print(map.tag)

	carte.append( etree.Element("node") )

	print(etree.tostring(carte, pretty_print=True))

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py
#	def sauveCarte(a, f):
	assert 0, 'terminer'

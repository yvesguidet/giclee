# -*- coding: utf-8 -*-

from lxml import etree

import os

def lily(c, d):
	''' insère semaine, veille et lendemain'''

	print 'lily : c = {}'.format(c)
	print 'lily : d = {}'.format(d)

	nomLong = os.path.join(d, c)
	
	arbre = etree.parse(nomLong)

	x = arbre.xpath("/map/node")[0]
	nomCarte = x.get('TEXT')

	print 'lily : x = {}'.format(x)
	print 'lily : type(x) = {}'.format(type(x))
	print 'lily : nomCarte = {}'.format(nomCarte)

	assert 0, 'ouais ?'
	

#	print(map.tag)

	carte.append( etree.Element("node") )

	print(etree.tostring(carte, pretty_print=True))

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py
#	def sauveCarte(a, f):
	assert 0, 'terminer'

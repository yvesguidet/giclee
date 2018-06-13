# -*- coding: utf-8 -*-

from lxml import etree

import os

def insWeek(c, d):
	''' insère semaine, veille et lendemain'''

	print 'insWeek : c = {}'.format(c)
	print 'insWeek : d = {}'.format(d)

	nomLong = os.path.join(d, c)

	arbre = etree.parse(nomLong)

	x = arbre.xpath("/map/node")[0]
	nomCarte = x.get('TEXT')

	print 'insWeek : x = {}'.format(x)
	print 'insWeek : type(x) = {}'.format(type(x))
	print 'insWeek : nomCarte = {}'.format(nomCarte)


#	print(map.tag)

	verrue = etree.Element("node")
	verrue.set('TEXT', 'sem')
	x.append(verrue)

	# insertion du lien
	import datetime
	numSemCour =  datetime.date.today().isocalendar()[1]

	semSuiv = 'Sem{}18.mm'.format(numSemCour + 1)


	verrue.set('LINK', semSuiv)

	joliarbre = etree.tostring(arbre, pretty_print=True)

	#	print joliarbre

	import sys

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py
	sys.path.append('/home/yves/2011/dev/Python/XCartes/XNextWeek')

	from postTraitCHebdo import sauveCarte

#	def sauveCarte(a, f):
	sauveCarte(joliarbre, c)


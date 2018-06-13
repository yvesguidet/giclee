# -*- coding: utf-8 -*-

from lxml import etree

import os, glob

def veille(c, d):
	jours = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')
	trwa = c[:3]

	i = jours.index(trwa)
	
	if i == 0:
		return	# lundi : later
	assert 0, i

def insVeille(c, d):
	''' ins. veille '''
	nomLong = os.path.join(d, c)

	arbre = etree.parse(nomLong)

	x = arbre.xpath("/map/node")[0]
	nomCarte = x.get('TEXT')

#	print(map.tag)

	verrue = etree.Element("node")
	verrue.set('TEXT', 'hier')
	verrue.set('LINK', veille(c, d))
	assert 0, verrue

def insWeek(c, d):
	''' insère semaine, veille et lendemain'''

	nomLong = os.path.join(d, c)

	arbre = etree.parse(nomLong)

	x = arbre.xpath("/map/node")[0]
	nomCarte = x.get('TEXT')

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


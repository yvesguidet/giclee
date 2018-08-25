# -*- coding: utf-8 -*-

prod = True

jours = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

from lxml import etree

import sys

sys.path.append('/home/yves/2011/dev/Python/XCartes/XNextWeek')

from postTraitCHebdo import sauveCarte

import os, glob

import datetime

def numSemCour():
	return datetime.date.today().isocalendar()[1]

def insLend(c, d):
	'''ins. lendemain'''
	nomLong = os.path.join(d, c)

	arbre = etree.parse(nomLong)

	x = arbre.xpath("/map/node")[0]
	nomCarte = x.get('TEXT')

	verrue = etree.Element("node")
	verrue.set('TEXT', 'dem')
	l = lend(c, d)

	if l:
		assert l <> None
		from os.path import basename
		l = basename(l)
		assert not '/' in l
		verrue.set('LINK', l)

	x.append(verrue)
	joliarbre = etree.tostring(arbre, pretty_print=True)
	sauveCarte(arbre, c)
	#	assert 0, joliarbre

#	print(map.tag)

	#	assert 0, (c, d)

def lend(c, d):
	trwa = c[:3]

	i = jours.index(trwa)
	if i == 6:
		return # None (pour dimanche)
	dem = jours[i + 1]
	x = os.path.join(dem + '*.mm')
	d = glob.glob(x)[0]	# 2do vérif 1 et 1 seul

	return d

def veille(c, d):
	#	jours = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')
	trwa = c[:3]

	i = jours.index(trwa)

	if i == 0:
		return	# lundi : later
	hier = jours[i - 1]

	x = os.path.join(d, hier + '*.mm')
	l = glob.glob(x)
	assert len(l) == 1

	return l[0]

def insVeille(c, d):
	''' ins. veille '''
	nomLong = os.path.join(d, c)

	arbre = etree.parse(nomLong)

	x = arbre.xpath("/map/node")[0]
	nomCarte = x.get('TEXT')

#	print(map.tag)

	verrue = etree.Element("node")
	verrue.set('TEXT', 'hier')
	v = veille(c, d)
	if v:
		from os.path import basename
		v = basename(v)
		assert not '/' in v
		verrue.set('LINK', v)

	x.append(verrue)
	joliarbre = etree.tostring(arbre, pretty_print=True)
	sauveCarte(arbre, c)


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

	nsc =  numSemCour()

	semSuiv = 'Sem{}18.mm'.format(nsc + 1)

	verrue.set('LINK', semSuiv)


	#	print joliarbre

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py

#	def sauveCarte(a, f):
	assert isinstance(arbre, etree._ElementTree)
	sauveCarte(arbre, c)

sys.path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/recurre')

from nodes import zoli

from chTexteCarte import chTexteCarte

#	def chTexteCarte(j3, semSuiv):
#		arbre = etree.parse(semSuiv)
#		elements = arbre.findall('.//node')	# XPath, recursive.
#		#	assert 0, len(elements)
#		for e in elements:
#			zoli(e, impr = True)
#
#			assert 0, e


def majLienDsSuiv(cartej3AsString, repertoire):
	''' màj lien sur cartej3AsString ds sem suiv (was lily) '''

	#	assert 0, repertoire

	#	sys.path.append('/home/yves/2011/dev/Python/XCartes/XNoeud/nodes-dev/')


	n = numSemCour()

	#	assert d == '/home/yves/2011/dev/Python/outils/mmNextWeek/essais/'

	import datetime
	numSemSuiv =  n + 1
	semSuiv = 'Sem{}18.mm'.format(numSemSuiv)

	import os

	semSuiv = os.path.join(repertoire, semSuiv)

	assert repertoire ==	'/home/yves/2011/dev/Python/XCartes/XNextWeek/essais/'
	assert os.path.exists(semSuiv), 'majLienDsSuiv : {} non trouvé (lancer XNextWeek ?)'.format(semSuiv)

	j3 = cartej3AsString[0:3]

	semSuivAsTree = chTexteCarte(cartej3AsString, semSuiv)


	zoli(semSuivAsTree, impr = True)
	sauveCarte(semSuivAsTree, semSuiv)

	return

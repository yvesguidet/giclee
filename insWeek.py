# -*- coding: utf-8 -*-

bavard = True

from lxml import etree

import sys

sys.path.append('/home/yves/2011/dev/Python/XCartes/XNextWeek')

from postTraitCHebdo import sauveCarte

import os, glob

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
	if bavard:
		print 'insWeek.insLend : arbre = {}'.format(arbre)
		print 'insWeek.insLend : type(arbre) = {}'.format(type(arbre))
	joliarbre = etree.tostring(arbre, pretty_print=True)
	sauveCarte(arbre, c)
	#	assert 0, joliarbre

#	print(map.tag)

	#	assert 0, (c, d)

def lend(c, d):
	jours = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')
	trwa = c[:3]

	i = jours.index(trwa)
	if i == 6:
		return # None (pour dimanche)
	dem = jours[i + 1]
	x = os.path.join(dem + '*.mm')
	d = glob.glob(x)[0]	# 2do vérif 1 et 1 seul

	return d

def veille(c, d):
	jours = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')
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
	import datetime
	numSemCour =  datetime.date.today().isocalendar()[1]

	semSuiv = 'Sem{}18.mm'.format(numSemCour + 1)

	verrue.set('LINK', semSuiv)


	#	print joliarbre

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py

#	def sauveCarte(a, f):
	assert isinstance(arbre, etree._ElementTree)
	sauveCarte(arbre, c)

def lily(c, d):
	''' màj lien  '''

	assert d == '/home/yves/2011/dev/Python/outils/mmNextWeek/essais/'

	import datetime
	numSemSuiv =  datetime.date.today().isocalendar()[1] + 1
	semSuiv = 'Sem{}18.mm'.format(numSemSuiv)

	import os

	semSuiv = os.path.join(d, semSuiv)

	from nodes import noeudsAyantValeur

	l = noeudsAyantValeur(semSuiv, 'TEXT', 'lun')
	assert 0, l

# -*- coding: utf-8 -*-

jours = ('lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim')

from lxml import etree

import sys

sys.path.append('/home/yves/2011/dev/Python/XCartes/XNextWeek')

from postTraitCHebdo import sauveCarte

import os, glob

import datetime

def numSemCour(d = datetime.date.today()):
	return d.isocalendar()[1]

def annee2chiffres(d = datetime.date.today()):
	return d.isocalendar()[0] - 2000

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

	a = annee2chiffres()

	semSuiv = 'Sem{:02d}{}.mm'.format(nsc + 1, a)

	verrue.set('LINK', semSuiv)


	#	print joliarbre

# /home/yves/2011/dev/Python/XCartes/XNextWeek/postTraitCHebdo.py

#	def sauveCarte(a, f):
	assert isinstance(arbre, etree._ElementTree)
	sauveCarte(arbre, c)

sys.path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/recurre')

from nodes import zoli

from injJourSSuiv import injJourSSuiv

def lanceXN():
	''' lance XN*y'''

	import os

	k = 'cd /home/yves/2011/dev/Python/XCartes/XNextWeek; ./XNextWeek.py'
	os.system(k)

def majLienDsSuiv(cartej3AsString, repertoire):
	''' màj lien sur cartej3AsString ds sem suiv (was lily) '''

	assert not 'essais' in repertoire
	assert 'essai' in repertoire

	n = numSemCour()

	#	assert d == '/home/yves/2011/dev/Python/outils/mmNextWeek/essais/'

	import datetime
	numSemSuiv =  n + 1
	if n != 52:
		semSuiv = 'Sem{:02d}18.mm'.format(numSemSuiv)
	else:
		numSemSuiv = 1
	semSuiv = 'Sem{:02d}19.mm'.format(numSemSuiv)

	import os

	semSuiv = os.path.join(repertoire, semSuiv)

	assert repertoire == '/home/yves/2011/dev/Python/outils/giclee/essai'
	#	assert os.path.exists(semSuiv), 'majLienDsSuiv : {} non trouvé (lancer XNextWeek ?)'.format(semSuiv)

	lanceXN()

	j3 = cartej3AsString[0:3]

	semSuivAsTree = injJourSSuiv(cartej3AsString, semSuiv)


	#	zoli(semSuivAsTree, impr = True)
	sauveCarte(semSuivAsTree, semSuiv)

	return

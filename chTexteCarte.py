#!  /usr/bin/env python
# -*- coding: utf-8 -*-

# vendredi 24 août 2018, 07:27:30 (UTC+0200)

from sys import path

path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/recurre')

from lxml import etree

from nodes import zoli

def chTexteCarteAux(j, arbre):
	assert not isinstance(arbre, str)
	assert len(j) > 3

	j3 = j[0:3]

	#	assert 0, j3

	elements = arbre.findall('.//node')	# XPath, recursive.
	#	print len(elements)
	for e in elements:
		t = e.get('TEXT')

		if t == None:
			return
		troisPremiers = t[:3]
		if troisPremiers == j3:
			#	zoli(e, impr = True)
			l = e.get('LINK')

			print '*** chTexteCarteAux() j3 = {}, l = {}, j = {}'.format(j3, l, j)
			# tataaaaaaaaaaaaaaaaa
			e.set('LINK', j)
			##########################
#	sauveCarte(arbre, c)
			##########################
			return

def chTexteCarte(j3, semSuiv):
	arbre = etree.parse(semSuiv)
	chTexteCarteAux(j3, arbre)

if __name__ == '__main__':
	chTexteCarte('jeu23_sem34', "essais-XNextWeek/Sem3518.mm")

#!  /usr/bin/env python
# -*- coding: utf-8 -*-

# vendredi 24 août 2018, 07:27:30 (UTC+0200)

from sys import path

path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/recurre')

from lxml import etree

from nodes import zoli

def chTexteCarteAux(jour, arbre):
	'''chTexteCarteAux : injecte jour ds arbre (sem suiv)'''
	assert not isinstance(arbre, str)
	assert len(jour) > 3

	j3 = jour[0:3]

	elements = arbre.findall('.//node')	# XPath, recursive.
	#	print len(elements)
	for e in elements:
		t = e.get('TEXT')

		if t == None:
			return arbre
		troisPremiers = t[:3]
		if troisPremiers == j3:
			#	zoli(e, impr = True)
			l = e.get('LINK')

			print '*** chTexteCarteAux() j3 = {}, l = {}, jour = {}'.format(j3, l, jour)
			# tataaaaaaaaaaaaaaaaa
			e.set('LINK', jour)
			##########################
#	sauveCarte(arbre, c)
			##########################
			return arbre

def injJourSSuiv(j, semSuiv):
	'''injJourSSuiv : injecte jour ds sem suiv'''
	arbre = etree.parse(semSuiv)
	return chTexteCarteAux(j, arbre)

if __name__ == '__main__':
	injJourSSuiv('jeu23_sem34', "essais-XNextWeek/Sem3518.mm")

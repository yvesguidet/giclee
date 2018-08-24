#!  /usr/bin/env python
# -*- coding: utf-8 -*-

# vendredi 24 août 2018, 07:27:30 (UTC+0200)

from sys import path

path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/recurre')

from lxml import etree

from nodes import zoli

def scr(j3, arbre):
	assert not isinstance(arbre, str)

	elements = arbre.findall('.//node')	# XPath, recursive.
	print len(elements)
	for e in elements:
		t = e.get('TEXT')

		if t == None:
			return
		troisPremiers = t[:3]
		if troisPremiers == j3:
			#	zoli(e, impr = True)
			l = e.get('LINK')
			
			print 'scr() j3 = {}, l = {}'.format(j3, l)
			return

def chTexteCarte(j3, semSuiv):
	arbre = etree.parse(semSuiv)
	scr(j3, arbre)

if __name__ == '__main__':
	j3 = 'jeu'
	semSuiv = "essais-XNextWeek/Sem3518.mm"
	chTexteCarte(j3, semSuiv)

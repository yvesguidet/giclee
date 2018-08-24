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
	#	assert 0, len(elements)
	for e in elements:
		zoli(e, impr = True)
		assert 0
		scr(j3, e)

def chTexteCarte(j3, semSuiv):
	arbre = etree.parse(semSuiv)
	scr(j3, arbre)

if __name__ == '__main__':
	j3 = 'jeu'
	semSuiv = "essais-XNextWeek/Sem3518.mm"
	chTexteCarte(j3, semSuiv)

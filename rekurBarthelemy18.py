#!  /usr/bin/env python
# -*- coding: utf-8 -*-

# vendredi 24 août 2018, 07:27:30 (UTC+0200)

from sys import path

path.append('/home/yves/2011/dev/Python/outils/mmNextWeek/recurre')

from nodes import zoli

def chTexteCarte(j3, semSuiv):
	arbre = etree.parse(semSuiv)
	elements = arbre.findall('.//node')	# XPath, recursive.
	#	assert 0, len(elements)
	for e in elements:
		zoli(e, impr = True)

		assert 0, e

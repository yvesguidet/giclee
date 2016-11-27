# -*- coding: utf-8 -*-

from sys import path

path.append('/home/yves/2011/2016/automne/rentree/pymmPremCrochet')

from FinProvisoire import FinProvisoire
from os import system
import commands


def semCour():
	k = "grep -w ^sem params.py|tail -1"
	ligne = commands.getoutput(k)
	print "semCour : ligne = '{}'".format(ligne)
	mots = ligne.split("'")
	print "semCour : mots[1] = '{}'".format(mots[1])
	return mots[1]

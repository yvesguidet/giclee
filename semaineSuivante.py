#!  /usr/bin/env python
# -*- coding: utf-8 -*-

# samedi 29 décembre 2018, 09:36:29 (UTC+0100)

#	https://stackoverflow.com/questions/1622038/find-mondays-date-with-python

import datetime

def dem1(d = datetime.date.today()):
	''' '''
	dd = d + datetime.timedelta(days = 1, weeks = 0)
	return dd

def lundiDernier():
	''' lundi dernier '''
	today = datetime.date.today()
	ld = today + datetime.timedelta(days = -today.weekday(), weeks = 0)
	return ld

def lundiProchain():
	''' lundi prochain '''
	today = datetime.date.today()
	lp = today + datetime.timedelta(days = -today.weekday(), weeks = 1)
	#	print 'lundiProchain : lp = {}'.format(lp)
	return lp

if  __name__ == '__main__':

	#	print 'semaineSuivante : lundiProchain = {}'.format(lundiProchain())
	#	print 'semaineSuivante : lundiDernier = {}'.format(lundiDernier())
	#	print 'semaineSuivante : dem1 = {}'.format(dem1())
#	l = lundiDernier()
#	for d in range(7):
#		print 'semaineSuivante : dem1 = {}'.format(dem1(l))
#		l = dem1(l)
#	print # une ligne pour aérer
	l = lundiProchain()
	for d in range(7):
		print 'semaineSuivante : dem1 = {}'.format(l),
##
		from insWeek import numSemCour, annee2chiffres
#def numSemCour(d = datetime.date.today()):
#def annee2chiffres(d = datetime.date.today()):
##
		print 'sem = {}'.format(numSemCour(l)),
		print 'an = {}'.format(annee2chiffres(l))
		l = dem1(l)


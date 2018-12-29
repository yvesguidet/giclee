#!  /usr/bin/env python
# -*- coding: utf-8 -*-

# samedi 29 décembre 2018, 09:36:29 (UTC+0100)

#	https://stackoverflow.com/questions/1622038/find-mondays-date-with-python

import datetime

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

	print 'semaineSuivante : lundiProchain = {}'.format(lundiProchain())
	print 'semaineSuivante : lundiDernier = {}'.format(lundiDernier())


#!  /usr/bin/env python
# -*- coding: utf-8 -*-

def njm(m, a = 2018):
	'''nb jours du mois'''
	#
	import datetime
	d = datetime.date.today()	# auj
	d = d.replace(month = m, year = a, day = 28)
	print 'd = {}'.format(d)
	assert 0, 'use replace ok ?'

	while 1:
		d = dem1(d)
		print 'd = {}'.format(d)
		print 'type(d) = {}'.format(type(d))
		assert 0, 'finir'
	assert 0, 'finir'

if  __name__ == '__main__':
	print njm(11, 2018)

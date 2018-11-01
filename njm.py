#!  /usr/bin/env python
# -*- coding: utf-8 -*-

def njm(m, a = 2018):
	'''nb jours du mois'''

	#
	from sys import path
	path.append('/home/yves/2011/2018/automne/cartes/giclee/XNextWeek/giclee/lundis')
	#
	import datetime
	from ls import dem1
	d = datetime.date.today()	# auj
	a = int(str(d).split('-')[0])
	print 'a = {}'.format(a)
	print 'type(a) = {}'.format(type(a))
	assert m != 12
	d = d.replace(month = m, year = a, day = 28)
	#	print 'd = {}'.format(d)

	j = int(str(d).split('-')[2])
	#	print 'j = {}'.format(j)
	mm = int(str(d).split('-')[1])
	#	print 'mm = {}'.format(mm)
	return nz(m, j, a, d)
#		while 1:
#			d = dem1(d)
#			#	print 'd = {}'.format(d)
#			#	print 'type(d) = {}'.format(type(d))
#
#			mm = int(str(d).split('-')[1])
#			print 'mm = {}'.format(mm)
#
#			jj = int(str(d).split('-')[2])
#			print 'jj = {}'.format(jj)
#
#			jj = int(str(d).split('-')[2])
#			print 'jj = {}'.format(jj)
#			assert m == mm

	assert 0, 'finir'

def nz(m, j, a, d):
	''' aux njm'''
	bavard = False

	if bavard:
		print 'nz : m = {}'.format(m)
		print 'nz : j = {}'.format(j)
		print 'nz : d = {}'.format(d)
	
	from ls import dem1
	d = dem1(d)

	if bavard:
		print 'nz : d = {}'.format(d)
	mm = int(str(d).split('-')[1])
	if bavard:
		print 'mm = {}'.format(mm)

	if m != mm:
		return j

	jj = int(str(d).split('-')[2])
	if bavard:
		print 'jj = {}'.format(jj)

	return nz(m, jj, a, d)
	

if  __name__ == '__main__':
	#	print njm(11, 2018)
	#	print njm(10, 2018)
	#	print njm(2, 2018)
	print njm(12, 2018)

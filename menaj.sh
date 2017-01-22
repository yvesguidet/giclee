#! /bin/bash
 
#	rm -f $(diff -rs . cartes|grep identiques$|awk '{print $3}')
sem=4	# passer en arg.
rm -f *_sem$sem.mm

#! /bin/bash

#	rm -f $(diff -rs . cartes|grep identiques$|awk '{print $3}')
sem=5	# passer en arg.
rm -f *_sem$sem.mm

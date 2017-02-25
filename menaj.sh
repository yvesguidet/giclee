#! /bin/bash

#	rm -f $(diff -rs . cartes|grep identiques$|awk '{print $3}')
sem=$(./semCour/semCour.py)
rm -f *_sem$sem.mm

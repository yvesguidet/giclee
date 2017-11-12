#! /bin/bash

# lundi 16 octobre 2017, 09:51:54 (UTC+0200)
cp -a cartes essai
cd essai

k="rsync $non -utvl [^g]*.mm cartes/"

eval $k

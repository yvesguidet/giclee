#! /bin/bash
non=-n
k="rsync $non -utvl [^g]*.mm cartes/"

eval $k

#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

cd /home/jovyan/work/originals
git pull 
for n in *.ipynb; do
    if test -f ../$n; then
	echo $n already there
    else
	cp $n ../$n
    fi
done



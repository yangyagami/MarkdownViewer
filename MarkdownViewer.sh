#!/usr/bin/env bash

basedir=$(dirname "$0")
source $basedir/env/bin/activate
python $basedir/src/main.py $1

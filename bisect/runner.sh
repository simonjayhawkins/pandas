#!/bin/bash
python setup.py build_ext -i -j 2 || exit 125
python ../$1.py || exit 1

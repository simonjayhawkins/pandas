#!/bin/bash
python setup.py build_ext -i -j 2
python ../$1.py
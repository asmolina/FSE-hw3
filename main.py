#!/usr/bin/env python 3

from . import useful_package
import sys 

x = float(sys.argv[-1]) 

print(x, polynom_3(x), hyperbola(x))


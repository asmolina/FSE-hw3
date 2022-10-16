#!/usr/bin/env python3

import useful_package
import sys 

x = float(sys.argv[-1]) 

print(x, useful_package.module_a.polynom_3(x), useful_package.module_b.hyperbola(x))


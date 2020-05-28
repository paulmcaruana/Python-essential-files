#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = "seven"
# x = "seven '{1:<9}' '{0:>9}'".format(8, 9)
# x = "seven '{1:<09}' '{0:>09}'".format(8, 9)
a = 8
b = 9
x = f"seven {a} {b}" # this is an f string and only available on Python 3.6 and after. works exactly the same as using the .format way
print('x is {}'.format(x))
print(type(x))

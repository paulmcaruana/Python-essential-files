#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, "two", 3.0, [4, "four"], 5)
y = [1, "two", 3.0, [4, "four"], 5]
print('x is {}'.format(x))
print(type(x[1])) # this will tell us the type of the element at position 1 
print(id(x))
print(id(y))

# if x is y:
#     print("yep")
# else:
#     print("nope")
# 
# if x[0] is y[0]:
#     print("yep")
# else:
#     print("nope")

if isinstance(y, tuple):
    print("tuple")
elif isinstance(y, list):
    print("list")
else:
    print("nope")
    
if isinstance(x, tuple):
    print("tuple")
elif isinstance(x, list):
    print("list")
else:
    print("nope")
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = (1, 2, 3, 4, 5)
# y =  (6, 7, 8, 9, 10)
# z = zip(x, y)
# for a, b in z:
#     print(f'{a} - {b}')

x = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x):
    print(f'{i}: {v}')

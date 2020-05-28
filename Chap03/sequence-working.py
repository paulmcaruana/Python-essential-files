#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]   # this is a list and it is mutable
 # x[2] = 42
 
# x = (1, 2, 3, 4, 5 )   # this is a tuple and it is immutable

# x = range(5, 50, 5) # this is a range and the parameters are start, end and step. just two is start and end, just one is end.

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5} # this is a dictionary with keys and values respectively. They are mutable
x['three'] = 42
for k, v in x.items():
    print('k: {}, v:{}'.format(k, v))

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# this will help you call a function that is within a function, from outwith the top level function.
#f1 is a wrapper for f2 in range:
#     code
# 
# 
# def f1():
#     def f2():
#         print('this is f2')
#     return f2
#     
# x = f1()
# x()

def f1(f):
    def f2():
        print('this is before the function the function call')
        f()
        print("this is after the function call")
    return f2

@f1
def f3():
    print("this is f3")

f3()
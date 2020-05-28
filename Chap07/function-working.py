#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     x = [5]
#     kitten(x)
#     print(f"in main x is {x}")
# 
# def kitten(a):
#     a[0] = 3
#     print('Meow.')
#     print(a)
# 
# if __name__ == '__main__': main()

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    return dict(x = 42, y = 43, z = 44)

if __name__ == '__main__': main()
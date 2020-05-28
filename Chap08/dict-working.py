#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #     'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    
    # the above can also be written as:
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr',
                   giraffe = 'I am a giraffe!', dragon = 'rawr' )
    for k in animals.values(): print(k)
    # print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f"{k}: {v}")

if __name__ == '__main__': main()

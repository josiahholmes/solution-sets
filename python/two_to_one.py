#!/usr/bin/env python3


'''
Take 2 strings s1 and s2 including only letters 
from a to z. Return a new sorted string, the longest 
possible, containing distinct letters,

each taken only once - coming from s1 or s2. 
#Examples: ``` a = 'xyaabbbccccdefww' b = 'xxxxyyyyabklmopq' 
# longest(a, b) -> 'abcdefklmopqwxy'
'''


def longest(s1, s2):
    print(''.join(sorted(set(s1 + s2))))


# Tests
longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq') # abcdefklmopqwxy
longest('aretheyhere', 'yestheyarehere') # aehrsty
longest('loopingisfunbutdangerous', 'lessdangerousthancoding') # abcdefghilnoprstu
longest('inmanylanguages', 'theresapairoffunctions') # acefghilmnoprstuy
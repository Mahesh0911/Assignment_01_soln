'''
Write a Python program to generate all permutations of a list in Python.
'''

from itertools import permutations


li=['abc', 'xyz', 'aba', '1221']

per=permutations(li)

for i in per:
    print(i)


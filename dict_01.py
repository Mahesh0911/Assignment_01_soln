'''
Write a Python script to sort (ascending and descending) a dictionary by
value.
'''

from typing import OrderedDict


dict={'c':3,'a':1,'e':5,'b':2,'d':4,'f':6}

dict=OrderedDict(sorted(list(dict.items())))

print(sorted(dict))

print(dict)
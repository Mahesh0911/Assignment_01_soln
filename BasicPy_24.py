'''
Write a Python program to get the size of an object in bytes.
'''
from ctypes import sizeof
from genericpath import getsize
import sys

i=22

print(sys.getsizeof(i))
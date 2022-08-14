'''
 Write a Python program to check whether a file exists.
'''
import os

if os.path.exists('text.txt'):
    print("file exists.")
else:
    print("file doesn't exists.")
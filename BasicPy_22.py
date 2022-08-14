'''
Write a Python program to get the command-line arguments (name of the script, the number
of arguments, arguments) passed to a script
'''

import sys

length=len(sys.argv)

print("Number of arguments :",length)

for i in sys.argv:
    print(i)



'''
Write a Python program to count number of items in a dictionary value
that is a list.
'''

from typing import is_typeddict


dict={1: 10, 2: 20, 3: 30, 4: 40, 5: [50,33], 6: [60]}
count=0

for i in dict.values():
    if(type(i)==list):
        count+=1
    
print(count)
'''
Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
'''

import array
arr=array.array('i',[2,3,5,7,5,3,1,9])

for i in range(0,len(arr)):
    print(arr[i],end=" ")

print()
print(arr[3])

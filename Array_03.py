'''
Write a Python program to get the number of occurrences of a specified element in an
array.
'''

lst=[3,4,1,3,5,7,5,3,2,1,6,7,8,3,1,4,2,1]

ch=3

count=0
for i in lst:
    if(i==ch):
        count+=1

print(count)
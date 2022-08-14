'''
Write a Python program to find maximum and the minimum value in a set.
'''
set1={1,2,5,7,9,6,3,4,0,10}

print ("set1 =",set1)
max=0
min=99

for i in set1:
    if(i > max):
        max=i
    if i<min :
        min=i

print("maximum :" ,max)
print("minimum :" ,min)
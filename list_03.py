'''
 Write a Python program to get the smallest number from a list.
 '''
 
list=[2,4,6,4,1,2,9,0,7]

smallest=100
for i in list:
    if (i < smallest):
        smallest=i
print("smallest number is : ",smallest)
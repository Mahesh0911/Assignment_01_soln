'''
Write a Python program to create a symmetric difference.
'''

set1={1,2,5,7,9,6,3,4}
set2={3,6,8,0,5,3,1}

print ("set1 =",set1)
print ("set2 =",set2)

print("symmetric difference is : ",set1.symmetric_difference(set2))
print("symmetric difference is : ",set2.symmetric_difference(set1))
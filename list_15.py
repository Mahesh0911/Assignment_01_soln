'''
Write a Python program to find common items from two lists.
'''


l1=[1,3,6,7,8]
l2=[2,3,5,9,0]

l3=set(l1)
l4=set(l2)


print("Common elements are :",l3.intersection(l4))


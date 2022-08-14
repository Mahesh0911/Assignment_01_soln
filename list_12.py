'''
Write a Python program to get the difference between the two lists.
'''

l1=[1,3,6,7,8]
l2=[2,3,5,9,0]

l3=set(l1)
l4=set(l2)

l5=l3.symmetric_difference(l4)
l5=list(l5)

print(l5)
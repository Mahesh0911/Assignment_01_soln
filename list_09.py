'''
Write a Python function that takes two lists and returns True if they have at
least one common member.
'''



l1=[1,3,6,7,8]
l2=[2,3,5,9,0]

l3=set(l1)
l4=set(l2)

if(l3.intersection(l4)):
    print("Common elements are :",l3.intersection(l4))
    print(True)



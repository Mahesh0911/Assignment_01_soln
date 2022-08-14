'''
Write a python program to check whether two lists are circularly identical.
'''

l1=[1,3,6,7,8]
l2=[7,8,1,3,6]

def circularly_identical(list1, list2):
    
    return(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))

print(circularly_identical(l1,l2))

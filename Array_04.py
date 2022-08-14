'''
Write a Python program to remove the first occurrence of a specified element from an
array.
'''

lisst=[3,4,5,1,7,8,9,0,6,4,1,2,3,4,1]

ch=1

for i in range(0,len(lisst)):
    if(lisst[i]==ch):
        lisst.remove(lisst[i])
        break

print(lisst)

print(len(lisst))

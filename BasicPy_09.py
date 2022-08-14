'''
 Write a Python program to concatenate all elements in a list into a string and return it
'''
list1=["hello",1,3.14,"hii",True]

strin=""
for i in list1:
    strin+=(str)(i)

print(strin)

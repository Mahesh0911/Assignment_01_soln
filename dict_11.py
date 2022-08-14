'''
Write a Python program to convert a list into a nested dictionary of keys.
'''

lst=[1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60]

dic=dict()

for i in range(0,len(lst),2):
    dic.update({lst[i]:lst[i+1]})

print(dic)
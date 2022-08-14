'''
Write a Python program to find the list of words that are longer than n from a
given list of words(>2)
'''

list=['abc', 'xy', 'abacd', '1221']
num=2
str_li=[]

for i in list:
    if(len(i) > num):
        str_li.append(i)

print(list)
print(str_li)
'''
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

str='w3resource'
dict=dict()
for i in str:
    if(i in dict):
        dict[i]+=1
    else:
        dict.update({i:1})

print(dict)

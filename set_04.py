'''
Write a Python program to remove item(s) from set
'''

sett={1,3,5,7,6,4,3,7,8,9}

print(sett)

sett.remove(5)  #error if element not present
sett.discard(0)   # do nothing if element not present

print(sett)
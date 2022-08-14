'''
Write a Python program to check multiple keys exists in a dictionary.
'''

dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

keys=dict.keys()
k1={1,2,3}
print(k1.issubset(keys))

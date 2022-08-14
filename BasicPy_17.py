'''
Write a program to get execution time for a Python method.
'''

import time

t0=time.time()

for i in range(0,1000):
    print("Hello there !",i)

t1=time.time()

print("Estimated time :",t1-t0)
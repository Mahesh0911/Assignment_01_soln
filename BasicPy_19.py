'''
Write a Python program to get file creation and modification date/times.
'''

import os 
import time

path=r"helloWOrld.py"

ti_c=os.path.getctime(path)
ti_m=os.path.getmtime(path)

tc=time.ctime(ti_c)
tm=time.ctime(ti_m)

print("create time :",tc)
print("modification time :",tm)
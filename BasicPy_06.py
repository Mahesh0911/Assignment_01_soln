'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

from datetime import datetime


d1=datetime(2014,7,2)
d2=datetime(2014,7,11)

print(d2-d1)
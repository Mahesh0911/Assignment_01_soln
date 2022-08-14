''' 
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar

yy=int(input("Enter year :"))
mm=int(input("Enter month :"))
print(calendar.month(yy,mm,1,1))
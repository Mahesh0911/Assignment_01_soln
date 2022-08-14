'''
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

list1=[1,5,8,3]

num=int(input("Enter number to search in list :"))

if(num in list1):
    print(f"True : {num} Number is in list.")
else:
    print("False : Not in the list")
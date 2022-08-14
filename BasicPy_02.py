'''
Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

'''

print("Enter numbers using commas :")
list_str=input()

new_str_list=list_str.split(",")

print(type(new_str_list))
print(new_str_list)

print()

tuple_str=tuple(new_str_list)
print(type(tuple_str))
print(tuple_str)
'''
Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
l1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(l1)

l1.remove(l1[0])
l1.remove(l1[3])
l1.remove(l1[3])

print(l1)


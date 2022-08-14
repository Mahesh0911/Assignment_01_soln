# Write a Python program which accepts the user's first and last name and prints them in
# reverse order with a space between them.


print("Enter first name :")
f_name=input()

print("Enter last name :")
l_name=input()

rev_name=""
name=f_name+" "+l_name
len=len(name)
while(len>=0) :
    rev_name+=name[len-1]
    len=len-1
print (rev_name)
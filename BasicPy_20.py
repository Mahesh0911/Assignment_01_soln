'''
Write a Python program to sort three integers without using conditional statements and
loops.
'''
def sort(a,b,c):
    list1=[]
    list1.append(max(a,max(b,c)))
    d=list1[0]
    e=-max(-a,max(-b,-c))
    list1.append((a+b+c)-(d+e))
    list1.append(e)
    return list1

list2=sort(4,6,2)

print(list2)
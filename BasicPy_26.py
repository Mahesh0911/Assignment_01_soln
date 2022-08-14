'''
Write a Python program to count the number occurrence of a specific character in a string.
'''

str="dfkdjfkajeoirwrfjlakndkjanfjsdbgkl.ksahekjr"
count=0
ch='.'
for i in str:
    if(ch==i):
        count+=1

print(count)
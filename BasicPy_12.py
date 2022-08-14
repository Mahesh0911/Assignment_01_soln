'''
Write a python program to call an external command in Python.
'''

import subprocess
def r1():
    for i in range(1, 3):
        print(f"Hello world {i}")

result = subprocess.run(['python'], input=r1(), capture_output=True, encoding='UTF-8')

# print(result.stdout)
# print(result.stdout)

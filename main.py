'''
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Satyajeet Behera')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import array as ar
from array import *
val = array('i', [0, -1, 2, 3, -4, 5, 6, 7, -8, 9])
for i in range(len(val)):
    print(val[i])

vls = array('i', [0, -1, 2, 3, -4, 5, 6, 7, -8, 9])
for e in vls:
    print(e)

als = array('u', ['a', 'e', 'i', 'o', 'u'])
for i in als:
    print(i)
value = array('i', [0, -1, 2, 3, -4, 5, 6, 7, -8, 9])
newARR = array(value.typecode, (a*a for a in value))
for e in newARR:
    print(e)

arr = array('i', [])
n = int(input('enter the length of the array'))
for i in range(n):
    x = int(input('enter the next value'))
    arr.append(x)
print(arr)
val = int(input("enter the value for search"))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1
print(arr.index(val))
'''
string1 = "Geeks"
string2 = "For"


def print_func(string1, string2):
    print(string1, string2, string1, sep='$', end='$')


print_func(string1, string2)
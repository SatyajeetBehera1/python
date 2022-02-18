# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from numpy import *

arr1 = array([
    [1, 2, 3, 4, 5, 6],
    [4, 5, 6, 3, 2, 1]
])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2 = arr1.flatten()
print(arr2)
arr3 = arr2.reshape(1, 6, 2)
print(arr3)

m = matrix('1 2 3; 4 5 6; 7 8 9')
n = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
print(m.max())
x = m * n
print(x)


def greet():
    print('hello')
    print('good morning')


greet()


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(5, 4)
print(result1, result2)


def update(x):
    x = 8
    print(x)


a = 10
update(a)
print('a', a)

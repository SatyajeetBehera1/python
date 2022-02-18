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

arr = array([1, 2, 3, 4, 5], float)
print(arr)

arr = arange(0, 15)
print(arr)

arr = logspace(1, 40, 5)
print(arr)

arr = ones(5)
print(arr)

arr = linspace(0, 12)
print(arr)

arr = zeros(5)
print(arr)

arr = array([1, 2, 3, 4, 5])
i = 1
while i <= 5:
    print(i + 5)
    i = i + 1
arr = array([1, 2, 3, 4, 5])
for i in arr:
    print(i + 5)

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 4, 3, 2, 1])
arr = arr1 + arr2
print(min(arr))

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 4, 3, 2, 1])
print(concatenate([arr1, arr2]))

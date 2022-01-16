from functools import *
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
# from functools import *

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n * 2, evens))
add = reduce(lambda a, b: a + b, double)
print(evens)
print(double)
print(add)


def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div = smart_div(div)
div(2, 9)


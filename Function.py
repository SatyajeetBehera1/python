import random


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

# Print multiline instruction
# perform string concatenation of string
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


def person(name, age):
    print(name)

    print(age)


person('satyajeet', 18)


def add_sub(x, y):
    c = x + y
    d = x - y
    print(c)
    print(d)


add_sub(2, 3)


def sum(*b):
    x = 0
    for i in b:
        x = x + i
    print(x)


sum(1, 2, 3, 4, 5, 6, 7, 8, 9)


def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, '=', j)


person("satyajeet", age=18, city='talcher', mob=23456789765432)

x = 1234567890
print(f'{x:,}')

a = 10
print(id(a))


def something():
    a = 9
    x = globals()['a']


print(id(x))
print('in fun')
globals()['a'] = 15

import array as ar
from array import *


def count(list):
    even = 0
    odd = 0
    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = count(y)
print('even : {} and odd : {}'.format(even, odd))


def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    if n < 0:
        print("error")
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


fib(5)


def factorial(n):
    t = 1
    for i in range(1, n + 1):
        t = t * i
    print(t)


factorial(9)

n = int(input('enter the number'))
fib(n)

x = array('i', [])
n = int(input('enter the number'))
for i in range(n):
    y = int(input('enter the number'))
    x.append(y)
print(x)
even, odd = count(x)
print('even : {} and odd : {}'.format(even, odd))

import math
import cmath

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('satyajeet')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

while True:
    opr = {"1 for Addition": "+\n",
           "2 for Subtraction": "-\n",
           "3 for Multiplication": "*\n",
           "4 for Division": "/\n",
           "5 for trigonometric": "pi\n",
           "6 for power": "B\n",
           "7 for quadratic roots": "b\n",
           "8 for Exit": "B\n"}
    print("Which of these operations you need to perform:")
    print(opr.keys())

    A = input("Enter the operator: ")

    if A == "1":
        j = 0
        x = []
        for i in range(10):
            y = float(input("enter the number"))
            if y == 00:
                break
            x.append(y)
        print(x)
        for k in range(len(x)):
            j = j + x[k]
        print("sum of all number is : \n", j)
    elif A == "2":
        j = 0
        x = []
        for i in range(10):
            y = float(input("enter the number"))
            if y == 00:
                break
            x.append(y)
        print(x)
        for k in range(len(x)):
            j = j - x[k]
        print("Subtraction of all number is : \n", j)

    elif A == "3":
        j = 1
        x = []
        for i in range(10):
            y = float(input("enter the number"))
            if y == 00:
                break
            x.append(y)
        print(x)
        for k in range(len(x)):
            j = j * x[k]
        print("Multiplication of all number is : \n", j)
    elif A == "4":
        B = float(input("Enter first Number :"))
        C = float(input("Enter second Number :"))
        print("The result is: ")
        print(B / C)
    elif A == "5":
        opr = {"1 for sin": "+\n",
               "2 for cos": "-\n",
               "3 for tan": "*\n",
               "4 for cosec": "/\n",
               "5 for sec": "\n",
               "6 for cot": "B\n",
               "7 for Exit": "B\n"}
        print("Which of these operations you need to perform:")
        print(opr.keys())

        D = input("Enter the operator: ")
        if D == "1":
            E = int(input("enter the angle"))
            print(math.sin(E))
        if D == "2":
            E = int(input("enter the angle"))
            print(math.cos(E))
        if D == "3":
            E = int(input("enter the angle"))
            print(math.tan(E))
        if D == "4":
            E = int(input("enter the angle"))
            print(1 / math.sin(E))
        if D == "5":
            E = int(input("enter the angle"))
            print(1 / math.cos(E))
        if D == "6":
            E = int(input("enter the angle"))
            print(1 / math.tan(E))
        elif D == "7":
            continue
    elif A == "6":
        B = float(input("enter the base number"))
        D = float(input("enter the power number"))
        print("The result is :")
        print(B ** D)
    elif A == "7":
        a = float(input("enter the first value"))
        b = float(input("enter the second value"))
        c = float(input("enter the third value"))
        dis = (b ** 2) - (4 * a * c)
        ans1 = (-b - cmath.sqrt(dis)) / (2 * a)
        ans2 = (-b + cmath.sqrt(dis)) / (2 * a)
        print('The roots are')
        print(ans1)
        print(ans2)
    elif A == "8":
        break

# new code
x = 1
while x <= 10:
    y = int(input('enter the number\n'))
    if y < 18:
        print('you guess lesser number\nChance left', x)
    elif y > 18:
        print('you guess bigger number\nChance left', x)
    elif y == 18:
        print('you guess it right\nChance left', x)
        break
    x = x + 1
if x > 10:
    print('you loose')
"""


def sum(*b):
    x = 0
    for i in b:
        x = x + i
    return x


print(sum(21, 45, 23, 98, 65, 34, 78, 98, 54, 23))


j = 0
x = []
for i in range(5):
    n = int(input("enter the number"))
    x.append(n)
print(x)
sum(x)
for k in range(0, len(x)):
    j = j + x[k]
print(j)
"""

a = []
for i in range(10):
    a.append(i*++i)

for a[i] in a:
    print(a[i])


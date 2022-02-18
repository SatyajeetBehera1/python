import random
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


number = "1234567890"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower = "qwertyuiopasdfghjklzxcvbnm"
symbol = "!@#$%^&*(){}[];:.?"
length = 8
total = lower + upper + number + symbol
password = "".join(random.sample(total, length))
print("the password generated is :", password)

x = []
# j = len(x)
for i in range(5):
    y = float(input("enter the number\n"))
    if y == 45:
        break
    x.append(y)

print(x)

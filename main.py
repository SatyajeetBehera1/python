from time import sleep
from threading import *

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


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(.1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(.1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.02)
t2.start()
t1.join()
t2.join()
print('buy')

pos = -1


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


x = [1, 2, 3, 4, 5]
y = 5
if search(x, y):
    print("found at", pos + 1)
else:
    print("not found")


def found(list, n):
    i = 0
    u = len(list) - i
    while i <= u:
        mid = (i + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                i = mid + i
            else:
                u = mid + i
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 44
if found(list, n):
    print('found at', pos + 1)
else:
    print('not found')


def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                #print(nums)


nums = [423, 432524542, 87654678907654789076546, 5, 456536, 57624, 234536, 354231, 4256423, 254632413452, 653426,
        635765435345335, 24554245]
sort(nums)
print(nums)


def sorts(nums):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


nums = [4, 25, 6, 3, 7, 9]
sort(nums)
print(nums)


def sum(n):
    total = 0
    for index in range(n + 1):
        total += index
    return total


result = sum(100)
print(result)


def EvenAndOdd(arr, n):
    j = -1
    for i in range(0, n):
        if arr[i] % 2 == 0:
            j = j + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


arr = [12, 10, 9, 45, 2, 10, 10, 43]
n = len(arr)
EvenAndOdd(arr, n)
for i in range(0, n):
    print(arr[i], end=" ")


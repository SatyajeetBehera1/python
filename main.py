# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Satyajeet Behera')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config is', self.cpu, self.ram)


com1 = computer('i5', 16)
com2 = computer('ryzen5', 8)
com1.config()
com2.config()


class Car:
    wheel = 4

    def __init__(self):
        self.mil = 10
        self.comp = 'BMW'


c1 = Car()
c2 = Car()

Car.wheel = 5
c1.mil = 8
print(c1.comp, c1.mil, c1.wheel)
print(c2.comp, c2.mil, c2.wheel)


class student1:
    school = 'aliens'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print('this is student class..in abc module')


s1 = student1(83, 73, 84)
s2 = student1(88, 87, 65)

print(s2.avg())
print(student1.getschool())


class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.rollno, self.name)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.cpu, self.ram, self.brand)


p1 = student('satay', 1)
p2 = student('Shruti', 2)
p1.show()
p2.show()
lap1 = student.laptop()


class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')


class B:
    def __init__(self):
        print('in B init')

    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')


class C(B, A):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()


a1 = C()
a1.feature1()


class pycharm:
    def execute(self):
        print('compiling')
        print('running')


class myeditor:
    def execute(self):
        print('spell check')
        print('convention check')
        print('compiling')
        print('running')


class laptop:
    def code(self, ide):
        ide.execute()


ide = myeditor()
lap1 = laptop()
lap1.code(ide)


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)

        print(s3.m1, s3.m2)

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
            return s


s1 = student(58, 69)
s2 = student(60, 65)
s3 = s1 + s2

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

print(s1.sum(23 + 2323 + 232323))


class D:
    def show(self):
        print('in D show')


class E(D):
    def show(self):
        print("in E show")


a1 = E()
a1.show()


class top10:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = top10()
print(next(values))
for i in values:
    print(i)


def topten():
    n = 1
    while n <= 9:
        sq = n * n
        yield sq
        n = n + 1


values = topten()
for i in values:
    print(i)


def factorial(n):
    t = 1
    for i in range(t, n + 1):
        t = t * i
    print(t)


factorial(5)

a = 5
b = 0
try:
    print('resource open')
    print(a / b)
except Exception as e:
    print("hey,you can not divide a number by zero", e)
finally:
    print('resource closed')


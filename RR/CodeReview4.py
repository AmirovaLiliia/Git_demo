# def multi(a, b):
#     print(a * b)
# multi(5, 10)
#
#
# def multi(a, b):
#     return a*b
# print(multi(5, 10))
#
#
# def multi(a, b):
#     return a*b
# num = (multi(5, 10) + 10)
# num1 = (multi(10, 10))
# print(num)
# print(num1)
#
# def say_hello():
#     print('Hello')
# say_hello()
#
#
# def check_even(a):
#     if a % 2 == 0:
#         print('Yes')
#     else:
#         print('No')
# for i in range(15):
#         check_even(i)
#

# def check_even(a):
#     for i in range(a):
#         if i % 2 == 0:
#             print('Yes')
#         else:
#             print('No')
#
# check_even(10)
#
# def check_even(a):
#     lst = []
#     for i in range(a):
#         if i % 2 == 0:
#             lst.append('Yes')
#         else:
#             lst.append('No')
#     return lst
# print(check_even(10))
#
# check_even(10)

# def fun():
#     s = 'hello'
#     print(s)
#
# fun()
#
#
# def fun():
#     print(f'First {s}')
#
# s = 'hello'
# fun()
# print(f'second {s}')

#
# def fun():
#     s = 'Hi'
#     print(f'First {s}')
#
# s = 'hello'
# fun()
# print(f'second {s}')
#
#
# age = 17
#
# def print_age():
#     print(age)
#
# print(age)



# def print_age():
#     age = 17
#     print(age)
#
# print(age)

#
# def multi():
#     x = 10
#     y = 5
#
#     def sum_fun():
#             c = 20
#             print(x + y + c)
#     sum_fun()
#
# multi()


#
# def multi():
#     x = 10
#     y = 5
#
#     def sum_fun():
#             c = 20
#             print(x + y + c)
#     sum_fun()
#
# y = 5
# multi()
#

# def multi():
#     x = 10
#     print(x + y + c)
#
#     def sum_fun():
#             c = 20
#             print(x + y + c)
#     sum_fun()
#
# c = 30
# y = 5
# multi()


#
# def multi(a, b):
#     print(a * b)
#
# multi(2, 5)
#
#
# a, b, c = [1, 'Hello', 3.5]
# print(a, b, c)
#
#
# a, b, *c = [1, 'Hello', 3.5, True, 45, ]
# print(a, b, c)
#
# *a, b, c = [1, 'Hello', 3.5, False, 47]
# print(a, b, c)
#
# a, *b, c = [1, 'Hello', 3.5, False, 47]
# print(a, b, c)
#
#
#
# def func(a, b, c):
#     print(a, b, c)
#
# a = (True, 51, 'Hello')
# func(*a)
#
# def func(*args):
#     print(args)
#
# a1 = [True, 51, 'Hello', 7.8]
# func(a1)
#
#
# def func(*args):
#     print(args)
#
# a1 = [True, 51, 'Hello', 7.8]
# a2 = [67, 45]
# func(a1, a2, 546)
#


# def func(*args):
#     print(args)
#
# a1 = [True, 51, 'Hello', 7.8]
# a2 = [67, 45]
# a3 = {1: '12',
#       2: '67',
#       3: ' Hello'}
# func(a3)
#
# def fun(*args):
#     s = 0
#     print(args)
#     for i in args:
#         s += i
#     print(s)
# a = (1, 4, 7, 19, 10, 12)
#
# fun(*a)
#
# def fun(*args):
#     # lst = args
#     # name = args[0]
#     # lastname = args[1]
#     # fathername = args[3]
#     # age = args[2]
#     print(f'Hello, {args[0]} {args[3]}!')
#
# fun('Liliia', 'Amirova', 36, 'Mirsayatovna')
#
#
#
# def return_dict(**kwargs):
#     print(kwargs)
#
# return_dict(a=2, b=4, c=6)


#
# def return_dict(*args, **kwargs):
#     print(kwargs)
#     print(f"Return kwargs {kwargs}!")
#     print(f"Return args {args}!")
# return_dict(a=2, b=4, c=6)
# return_dict(1, 2, 3)


#
# def return_dict(*args, **kwargs):
#     print(kwargs)
#     print(f"Return kwargs {kwargs}!")
#     print(f"Return args {args}!")
# return_dict(1, 2, 3, a=2, b=4, c=6)
# # return_dict(1, 2, 3)

#
# def fun(x):
#     print(x)
#     fun(x+1)
#
# fun(1)
#

#
# def fun(x):
#     if x <= 10:
#         print(x)
#         fun(x+1)
#
# fun(1)

#
# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n
# print(fact(5))
#


#
# def fun(x):
#     return x**3
#
# print(fun(3))
#
# a = lambda x: x**3
# print(a(3))
#
# s = lambda x: x*x
# print(s(6))

#
# a = lambda  x: 'Chetnoe' if  x % 2 ==0 else 'Nechetnoe'
# print(a(6))
#
# a = [34, 2, 67, 54, 9]
# a.sort()
# print(a)
#
#
#
# a = [30, 2, 60, 54, 9]
# print(sorted(a, key=lambda x: x % 10))

#
# a = ['hello', 'bbb', 'ddd', 'xxx', 'aa']  #по алфавиту
# print(sorted(a, key=lambda x: x))
#
#
# a = [(1, 2), (2, 1), (3, 3)]
# print(sorted(a, key=lambda x: x[1]))
#
# a = [(1, 'ccc'), (1, 'cc'), (3, 'qq')]
# print(sorted(a, key=lambda x: (x, x[1])))

#
# def fun(num):
#     return num%10
# a = [44440, 101, 43, 98, 34, 845]
# print(sorted(a, key=fun))

#
# a = [40, 23, 34, 12, 87]
# print(sorted(a, key=lambda x: x%10))
#
# #
# # a = [40, 23, 34, 12, 87]
# # print(sorted(a, key=lambda x: x if x%10=0 else for x in range())
#
# a = ['qqq 23', 'qqq 12', 'rrr 8']
# print(sorted(a, key=lambda x: int(x.split()[1])))
#
# a = ['qqq 23', 'qqq 12', 'rrr 8']
# print(sorted(a, key=lambda x: (x.split()[0], int(x.split()[1]))))
#
# a = ['qqq 23', 'qqq 12', 'rrr 8']
# print(sorted(a, key=lambda x: (x.split()[0], -int(x.split()[1]))))
#
#

#
# a = '1 2 3 4 5'
# b = list(map(int, a.split()))
# print(b)
#
# a = 'hello aaa 1 2 3 4 5'
# b = list(map(str, a.split()))
# print(b)


# def fun(x):
#     return x**2
#
# def fun_n(x):
#     return x**3
#
# a = [1, 3, 5, 7, -67, -3]
# # a1 = list(map(str, a))
# print(a1)
# a2 = list(map(abs, a))
# print(a2)
# a3 = list(map(fun, a))
# print(a3)
# a3 = list(map(fun_n, a))
# print(a3)

def fun(x):

    return x>5

a = [12, 5, 7, 3, 2, 0, -5]
a1 = filter(fun, a)
print(*a1)


def fun(x):

    return x>5

a = [12, 5, 7, 3, 2, 0, -5]
a1 = list(filter(fun, a))
print(a1)
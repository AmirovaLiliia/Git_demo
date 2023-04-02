#Functions
#
# def calc(a,b):
#     return a*b
#
# print(calc(5,4))

#
# def calc(a,b=1):
#     return a*b
#
# print(calc(5))
#
# def person(age, f_name, l_name):
#     return f'Hello, My name is {f_name} {l_name}. I am {age}.'
# print(person(37, 'Liliia', 'Amirova'))
#
# def person(age, f_name, l_name):
#     return f'Hello, My name is {f_name} {l_name}. I am {age}.'
# print(person(f_name = 'Liliia', l_name = 'Amirova', age = 37))
#
# def person(f_name, l_name, age = 20):
#     return f'Hello, My name is {f_name} {l_name}. I am {age}.'
# print(person('Liliia', 'Amirova'))
#
#
# print(sum([5, 6, 7, 9]))
# print(min([5, 6, 7, 9]))
# # print(max([5, 6, 7, 9]))
#
# def pattern(length, char1, char2):
#     return (char1 + char2) * length + char1
#
# print(pattern(8, '*', '-'))
#
# def pattern(length, char2, char1 = '*'):
#     return (char1 + char2) * length + char1
#
# print(pattern(8, '-'))
#
# def pattern(length=8, char2 = '/', char1 = '*'):
#     return (char1 + char2) * length + char1
#
# print(pattern(char2 = '*', length=8, char1 = '/'))
#
# mult = lambda x, y: x*y
# print(mult(5, 6))


# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2, l))
# print(filtered)
#
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2, l))
# print(*filtered)
#
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, float), l))
# print(*filtered)
#
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, str), l))
# print(*filtered)
#
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, str) or isinstance(x, float), l))
# print(*filtered)
#
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: not isinstance(x, str), l))
# print(*filtered)
l1 = [1, 45, 45, 98, 23, 15]
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# # filtered = list(filter(lambda x: not isinstance(x, str), l))
# # print(*filtered)
# power = list(map(lambda x: x**2, l1))
# print(power)
#
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# # filtered = list(filter(lambda x: not isinstance(x, str), l))
# # print(*filtered)
# power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
# print(power)
#
# # def calc(a,b):
#     return a*b
# result = calc(5,9)
# print(result)
#
#
# from functools import reduce
# result = reduce(lambda x, y: x - y, l1)
# print(result)

# def say_hello(name):
#     print(f'Hello, {name}!')
#
# def my_decorator(func):
#     def wrapper():
#         print('Я-обертка декоратора')
#         func()
#         print('Завернули')
#     return wrapper()
#
# def say_hello():
#     print(f'Hello')
#
# say_hello = my_decorator(say_hello)
# #
# # #или
# #
# # def my_decorator(func):
#     def wrapper():
#         print('Я-обертка декоратора')
#         func()
#         print('Завернули')
#     return wrapper()
# @my_decorator
# def say_hello():
#     print(f'Hello')
#
# def my_decorator(func):
#     def wrapper(arg):
#         print('Я-обертка')
#         func(arg)
#         print('Завернули')
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
#
# # say_hello('Sam')
#
#
# def milk(func):
#     def wrapper():
#         print('Hot milk')
#         func()
#     return wrapper
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
# @sugar #можно использовать много декораторов (sugar и milk)
# @milk
# def coffee():
#     print('Coffee')
# coffee()
#
#
# import time
# print(time.time())
#
# import datetime
# print(datetime.date.today())
# bdate = 1986
# current_date = datetime.date.today()
# current_month = current_date.month
# age = current_date.year - bdate
# print(age)
# print(current_month)

import math
import module
print(module.hello('Sam'))
from module import *

# from module import hello
# import module hello
# print('Hello ('Sam')')
import module math
print(sum(5, 28))

# print(dir(__builtins__))
# print(globals())
# print(f'Locals: {locals()}')


var = 'global'
def func1():
    def local():
        print(var)
    local()
func1()

var = 'global'
def func1():
    var = 'enclosed'
    def local():
        print(var)
    local()
func1()

var = 'global'
def func1():
    var = 'enclosed'
    def local():
        var = 'local'
        print(var)
    local()
func1()

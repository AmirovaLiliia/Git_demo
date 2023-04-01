# # compare = 3 == 3
# # print(compare)
#
# compare = 3 == 4
# print(compare)
#
# compare = 3 != 4
# print(compare)
#
# compare = 3 > 4
# print(compare)
#
# compare = 3 < 4
# print(compare)
#
# compare = 3 >= 4
# print(compare)
#
# compare = 3 <= 4
# print(compare)
#
# x = 3
# print(x > 3 and x < 8) #оба выражения истины
# print(x > 3 and x > 8) #одно из выражений ложно (но одно истино)
#
# print(x > 3 or x > 8) #одно из выражений истино
# print(x < 3 or x < 8) #хотя бы одно из выражений истино
#
# print(x > 3 and not x < 8) #оба выражения должны быть  истиныБ но только одно истино
# print(x > 3 and not x > 8) #оба выражения истины
import sys

# if x == 5:
#     print('Five')
# else:
#     print('Not five')

# if x != 5:
#     print('Five')
# else:
#     print('Not five')
#
# if x != 5:
#     print('Correct')
# else:
#     print('Not correct')
#
# if x == 5:
#     print('five')
# elif x > 5:
#     print('More than five')
# else:
#     print('Less than five')

# age = int(input ('Please, enter your age: '))
# if age >= 18:
#     print('Welcome')
# else:
#     print('Go home, baby!')

# num1 = int(input('Number1: '))
# num2 = int(input('Number2: '))
# operator = input('Operator: ')
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')
#
#
# num1 = int(input('Number1: '))
# num2 = int(input('Number2: '))
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/') or num1 > 5:
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')
#


# num1 = 0
# num2 = 0
# try:
#     num1 = int(input('Number1: '))
#     num2 = int(input('Number2: '))
# except ValueError:
#     print('Вы ввели не число!')
#     sys.exit()
# operator = input('Operator: ')
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')


# num = 0
# while num < 5:
#     print(num)
#     num = num + 1

# message = 'Hello'
# i = 1
# while i < 6:
#     print(i, message)
#     i += 1

# message = 'Hello'
# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i, message)
#     i += 1


# message = 'Hello'
# i = 1
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break
#     i += 1

# message = 'Hello'
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)

# message = 'Hello'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)
#
# message = 'Hello'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)


# for i in range(6):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(1, 6, 2):
#     print(i)


# for i in "Hello":
#     print(i)


# start = 5
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)


# def num():
#     return 2*2
# start = num()
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# i = 0
# x = 0
# while i < 4:
#     x += i
#     i += 1
#     print(x)

# i = 0
# x = 0
# while i < 5:
#     x += i
#     i += 1
#     print(f" x = {x}, i = {i}")


# message = 'Hello'
# if message:
#     print(message)
# else:
#     print('The string is empty')
#
# message = ''
# if message:
#     print(message)
# else:
#     print('The string is empty')

# num = 5
# if num%2:
#     print('Нечетное')
# else:
#     print('Четное')


# num = 5
# if num%2 != 0:
#     print('Нечетное')
# else:
#     print('Четное')

# def num(num1, num2):
#     return num1-num2
# print(num(10,5))
# print(num(9,6))

def num(num1, num2):
    return num1-num2
start = num(8,5)
stop = 15
step = 3
for i in range(start, stop, step):
     print(i)
#1.1
# max_xp = 100
# x = int(input())
# if max_xp - x >= 0:
#     print('Alive')
# else:
#     print('Dead')
#
# max_xp = 100
#
# def check_health(number):
#     while number >= 0:
#         print('Alive')
#     else:
#         print('Dead')
# #2.2.
# number = int(input('Enter your number: '))
# if number % 2 ==0:
#     print('Even')
# else:
#     print('Odd')
#
# #2.3
# num_year2 = int(input('Enter your year: '))
# if  num_year2 % 4 == 0 and num_year2 % 100 != 0 or num_year2 % 400 ==0:
#     print('Год високосный')
# else:
#     print('Невисокосный')
#

# #2.4
# text = input('Enter your text: ')
# row = int(input('amount of repeats: '))
# print((text + '\n') * row)
#
# text = input('Enter your text: ')
# row = int(input('amount of repeats: '))
# print(text * row)

#2.5

a = int(input('Введите первое число: ' ))
b = int(input('Введите второе число: ' ))
c = input('Введите оператор: ' )
if c == '+':
    d = a+b
    print(f'{a}+{b}={d}')
elif c == '-':
    d = a-b
    print(f'{a}-{b}={d}')
elif c == '*':
    d= a*b
    print(f'{a}*{b}={d}')
elif c == '/' and  b != 0:
    d= a/b
    print(f'{a}/{b}={d}')
elif c == '/' and b == 0:
    print('На ноль нельзя делить!')
else:
    print('Нечисло')






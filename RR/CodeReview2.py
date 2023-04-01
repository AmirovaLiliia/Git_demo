# s = 'hello world'
# print(s.replace('l', '?', 2))
#
# s = 'hello world'
# print(s.replace(' ', ''))
# print(s.count('o'))

# w = 'Денисов Денис Денисович'
# w1 = '1, 2, 3, 4, 5'
# print(w.split())
# print(w.split('е'))
# print(w1.split(','))
# print(w1.split(',', maxsplit=2))
# w2 = w1.split(',')
# print(''.join(w1))
# print(type(''.join(w1)))
# print('?'.join(w1))

# w3 = '    hello   '
# print(w3)
# print(w3.strip())
#
# w3 = '123hello123'
# print(w3)
# print(w3.strip('123'))

# w4 = 'hello world'
# print(w4.find('e'))
# print(w4.find('e', 2, 4))

# w5 = 'Hello'
# w5 = 'name world tiTle'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = '1234'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())

# w6 = 'QWERTy'
# w7 = 'QWERTY'
# w8 = '1234E'
# print(w6.isupp/er())
# print(w7.isupper())
# print(w8.isupper())

# w6 ='01234'
# w7 = '0,1'
# w8 = '1234E'
# print(w6.isdigit())
# print(w7.isdigit())
# print(w8.isdigit())

# w6 ='01234'
# w7 = 'QWERty'
# w8 = '1234E'
# print(w6.isalpha())
# print(w7.isalpha())
# print(w8.isalpha())

# a = int(input('Введите цифру: '))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} делится на 2 и на 10")
#     else:
#         print(f"{a} делится на 2, но не делится на 10")
# else:
#     print(f"{a} не делится на 2")

#
# q = int(input('Введите вашу отметку: '))
# if q >= 90:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >=70:
#     print(3)
# else:
#     print(2)10


# number = int(input('Введите число: '))
# if number < 10:
#     print('Однозначное число')
# elif 10 <= number < 99:
#     print('Двузначное число')
# elif 99 <= number <= 999:
#     print('Трехзначное число')
# else:
#     print('Большое число')

# x, y = 55, 50
# s = x if x > y else y
# print(s)
#
# x, y = 45, 50
# s = x if x > y else y
# print(s)

# value = 6
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print('Такой цифры нет!')

# c = 0
# while c < 5:
#     print('Hello')
#     c +=1

# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print('Chet')
#     else:
#         print('Nechet')
#     c +=1

# text = int(input('Введите число: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input('Для продолжения введите число, если не хотите, то введите stop ')
# print(f"Сумма чисел равна {count}")

# num = 10
# for i in range(num):
#     print(i)

# num = 10
# for i in range(1, num+1,):
#     print(i)
#
# num = 10
# for i in range(1, num+1, 2):
#     print(i)

# string1 = 'Hello'
# for i in range(len(string1)):
#     print(i)

# string1 = 'Hello'
# for i in range(len(string1)):
#     print(string1[i])
#
#
# string1 = 'Hello'
# for i in string1:
#     print(i)

# string1 = 'He3lL1o'
# for i in range(len(string1)):
#     if string1[i].islower():
#         print(i, string1[i])

# string1 = 'He3lL1o'
# for i in range(len(string1)):
#     if string1[i].isupper():
#         print(i, string1[i])

# string1 = 'He3lL1o'
# for i in range(len(string1)):
#     if string1[i].isdigit():
#         print(i, string1[i])

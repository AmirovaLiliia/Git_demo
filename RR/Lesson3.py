# my_list = [1, 'hello', 2.0, True, None]
# my_list = [1, 'hello', 2.0, True, None, 1, 1, 1]
# sentence = 'Python is awesome!'
# print(sentence.split(' '))
#
# sentence = 'Python is awesome!'
# print(sentence.split(' ', maxsplit=1))

# print(my_list[0])
# print(my_list[-1])
#
# my_list[0] = 25
# print(my_list)

# my_list.append(sentence)
# print(my_list)
# print(len(my_list))

# my_list.insert(0, sentence)
# print(my_list)
# my_list.insert(-2, sentence)
# print(my_list)

# print(my_list.count(1))

# print(my_list.index(1))
# print(my_list.index(None))

# my_list1 = [1, 2, 3, 4, 5]
# print(sum(my_list1))
# print(min(my_list1))

# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
# print(my_list1[-1])
# print(my_list1[-1] [-4])

# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [1, 2]]]
# print(my_list1[-1] [-1] [-2])
#
# my_list1.reverse()
# print(my_list1)

# For loop with list
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num**2)
#
# #another way

# new_l = [i*i for i in numbers if i%2]
# print(new_l)
#
# new_l = [i*i for i in numbers if i%2==0]
# print(new_l)
#
# new_l = [i for i in numbers if i%2==0]
# print(new_l)

# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))
#
#
# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple)

# name = 'Mark',
# print(name)

# my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

#Невозможно поменять, тк кортежи неизменяемая структура данных
# my_tuple[0] = 'ananas'
# print(my_tuple)
#но можно поменять структуру данных в лист и изменить в листе

# letters = list(my_tuple)
# letters[0] = 'ananas'
# print(letters)


# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple.index('name'))
# print(my_tuple.count('name'))
#
# my_tuple = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tuple if isinstance(item, int)])
# print(result)

# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of my_tuple is: {len(my_tuple)}')
# print(f'Length of result is: {len(result)}')
#
# for (index, item) in enumerate(my_tuple):
#     print(index, item)

# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1

# fruits = ('apple', ['ananas', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)

# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')

# def sum_it (*args):
#     total = 0
#     # print(args)
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))
# print(sum_it(4, 5, 10, 6, 20, 4, 5, 10, 6, 20))

def sum_it(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum

print(sum_it(5, 7, 12))

#или

def sum_it(num1, num2, num3):
    sum = num1 + num2 + num3
    print(sum)

sum_it(5, 7, 12)


# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append(item*item)
#     return l
# print(func(2, 5, 6, 8, 10))

#Dictionary
# my_dict = {}
# print(type(my_dict))
#
# my_dict = {
#     'name': 'Anna',
#     'last_name': 'Pavlova',
#     'age': 30,
#     'department': 'IT'
# }
# # print(my_dict)
# print(id(my_dict))
# print(my_dict['name'])
# print(my_dict['last_name'])
# print(my_dict.department)

# my_dict['last_name'] = 'Smirnova'
# print(my_dict['last_name'])
# print(my_dict)
# print(id(my_dict))

# print(len(my_dict))
#
# my_dict['salary'] = 5000
# print(my_dict)
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('salary'))
# print(my_dict.get('salary', 'Not found'))
#
#
# keys = ['name', 'salary', 'department']
# values = ['Alex', 50000, 'HR']
# employee = dict(zip(keys, values))
# print(employee)
#
# employee1 = dict(name='John', position='developer', salary=50000, department='IT', city='NY')
# print(employee1)

#SETS

# my_list = [1, 8, 2, 1, 1, 5, 5, 5, 8, 9]
# print(set(my_list))

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# print(set1.issubset(set2))  #сет1 не является подсножеством сет2 --> FALSE

# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# print(set1.issubset(set2))  #сет1  является подмножеством сет2 --> TRUE
#

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# print(set2.issuperset(set1))  #сет2  не является суперсетом сет1 ( не включает в себя сет1) --> FALSE

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# print(set2.intersection(set1))  #найти одинаковые значения
#
# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# print(set2.difference(set1))  #найти различные значения
# print(set1.difference(set2))
#
# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# print(set1.symmetric_difference(set2))  #найти неповторяющиеся значения
#

#
# set1 = {1, 2, 3, 'one', 'ten', 6}
# print(set1)
# print(id(set1))
# print(set1.remove(1))
# print(id(set1))
# print(set1.add(8))
# print(id(set1))
# print(set1)
#
# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)
# # set3 = {1, 2, 3}
# #
# #
#
# fs = frozenset({1, 2, 3})
# print(fs)
# fs.add(1)
# print(fs)
# # set3 = {1, 2, 3}
# #
#

# print(set1)
# set1 = {1, 2, 3, 'one', 'ten', 6}
# print(set1)
#
# my_list= [1, 9, 14, 'mango', 3, 4, 5, 'apple']
# print(set(my_list))


#Sort() and Sorted()
nums = [1, 2, 3, 5, 8, 9, 4, 0]
print(f'Initial list: {nums}')
print(id(nums))

print('SORTED()')
print(f'New sorted list: {sorted(nums)}')
print(f'Initial list after sorting: {nums}')
print(id(sorted(nums)))

print('.SORT()')
print(f'New sort list: {nums.sort()}') #NONE
print(f'New sort list after sorting: {nums}')
print(id(nums))

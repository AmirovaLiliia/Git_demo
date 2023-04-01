# # # list = [1, 2, 4, 7]
# # # print(list)
# # #
# # #
# # # list1 = []
# # # print(type(list1))
# #
# # # lst2 = list('3')
# # # lst2 = list(range(4))
# # # print(type(lst2))
# # #
# # # lst = [1, 2, 3, 'name', False, [1, 7, 9]]
# # # lst1 = [6, 7]
# # # print(type(lst))
# # # print(lst)
# # # print(len(lst))
# # # print(lst + lst1)
# # # print(2 in lst)
# # # print(0 in lst)
# # # print(lst[4])
# # # print(lst[5])
# #
# # # lst = [1, 4, 3, 5, 19, 10]
# # # print(sum(lst))
# #
# # # lst1 = [1, 4, 3, 5, 19, 10, 'name']
# # # print(sum(lst1))
# #
# # # print(max(lst))
# # # print(min(lst))
# # # print(lst.sorted())
# # # lst.sort()
# # # print(lst)
# # #
# # # print(sorted(lst))
# #
# # # lst1 = ['anna', 'dima']
# # #
# # # lst.append(45)
# # # print(lst)
# # #
# # # lst.extend(lst1)
# # # print(lst)
# #
# # # del lst[0]
# # # print(lst)
# #
# # # lst.clear()
# # # print(lst)
# # #
# # # lst.remove(19)
# # # print(lst)
# # #
# # # lst = [1, 4, 3, 5, 19, 10]
# # # lst1 = ['anna', 'dima']
# #
# # # a = lst.pop(3)
# # # print(a)
# # # print(lst)
# # #
# # #
# # # a = lst.pop()
# # # print(a)
# # # print(lst)
# # #
# # # lst.reverse()
# # # print(lst)
# #
# # # lst2 = lst.copy()
# # # print(lst)
# # # print(id(lst))
# # # print(lst2)
# # # print(id(lst2))
# #
# # # lst = [1, 2, 3]
# # # lst1 = lst
# # # # print(lst)
# # # print(lst1)
# # # print(id(lst))
# # # print(id(lst1))
# # # lst1 +=[100]
# # # print(lst)
# # # print(lst1)
# # # print(id(lst))
# # # print(id(lst1))
# # #
# # #
# # # lst = [1, 2, 3, 4]
# # # print(*lst)
# #
# # #или
# #
# # # lst = [1, 2, 3, 4]
# # # for i in lst:
# # #     print(i, end = ' ')
# #
# #
# # #
# # # lst = [1, 2, 3, 4, [34, 56]]
# # # print(*lst)
# #
# # #Генераторы списков
# # #[выражение for i in range(10]
# # # number = [i for i in range(10)]
# # # print(number)
# #
# # # number = [i for i in range(10) if i % 2 !=0]
# # # print(number)
# #
# # # number1 = [1, 2, 3]
# # # number2 = (1, 2, 3)
# # # number1[1] = 20
# # # number2[1] = 10
# # # print(number1)
# #
# # # number3 = (1, 2, 3
# # # print(type(number3))
# # # number4 = (1),
# # # print(type(number4))
# #
# # # lst = [1, 2, 3, 4, 5, 6]
# # # lst1 = (1, 2, 3, 4, 5, 6)
# # # print(lst.__sizeof__())
# # # print(lst1.__sizeof__())
# #
# # # a = (1, 2, 3)
# # # b = list(a)
# # # print(type(a))
# # # print(id(a))
# # # print(id(b))
# # # print(type(b))
# # # b[1] =15
# # # c = tuple(b)
# # # print(type(c))
# # # print(id(c))
# #
# # number = (1, 6, 4, 9, 2)
# # number1 = sorted(number)
# # print(number)
# # print(number1)
#
# #Sets
# # number = {1, 1, 5, 5, 4, 6, 3, 8}
# # print(number)
# # print(type(number))
# # number2 = {}
# # print(number2)
# # print(type(number2))
# #
# # print(sum(number))
# # sorted_number = sorted(number)
# # print(sorted_number)
# # number1 = set()
# # print(number1)
# # print(type(number1))
#
# # print(len(number))
# # print(min(number))
# # print(max(number))
# #
# # number = {1, 1, 5, 5, 4, 6, 3, 8, 'Hello', 'Hello'}
# # print(number)
# # for i in number:
# #     print(i)
# #
# # print(number[2]) # нельзя
#
# #
# # number1 = {1, 3, 4}
# # number2 = {1, 2, 3, 4, 5}
# # print(number == number1)
# # print(number == number2)
#
# # number4 = {1, 2, 3}
# # number5 = {6, 7, 9}
# # lst = [1, 'hello', False, [1, 3, 5]]
# # lst1 = [1, 'hello', False, (1, 3, 5)]
# # # number4.remove(6)
# # # number4.discard(6)
# # # number4.add(19)
# # # number4.update(number5)
# # # print(number4)
# # number5.update(lst)
# # number5.update(lst1)
# # print(number5)
# # #
# # my_set = {1, 2, 3, 4}
# # my_set2 = {3, 10, 18}
# # a = my_set.union(my_set2)
# # # print(a)
# # my_set = {1, 2, 3, 4}
# # my_set2 = {3, 10, 18}
# # a = my_set.intersection(my_set2)
# # print(a)
#
# # my_set = {1, 2, 3, 4}
# # my_set2 = {3, 10, 18}
# # a = my_set.difference(my_set2)
# # print(a)
# #
# # my_set = {1, 2, 3, 4}
# # my_set2 = {3, 10, 18}
# # a = my_set.symmetric_difference(my_set2)
# # print(a)
# #
# # set1 = {1, 2, 3, 4, 5}
# # set2 = {10, 30, 40}
# # print(set1.isdisjoint(set2))
# #
# # num = {int(i) for i in input()}
# # print(num)
# #
# # #Dict
# # dct = {
# #      'USA': '+1',
# #      'Russia': '+7',
# #      'Turkey': '+90'
# #     }
# # dct = {}
# # dct = dict(USA = +1, Russia = +7, Turkey = +90)
# # dct = dict([['USA', +1], ['Russia', +7], ['Turkey', +90]])
# #
# # print(dct)
# # print(type(dct))
# #
# # dct = {
# #     'USA': '+1',
# #     'Russia': '+7',
# #     'Turkey': '+90'
# # }
# # if 'USA' in dct:
# #     print('Yes')
# # else:
# #     print('No')
#
# #
# # dct = {
# #     'USA': '+1',
# #     'Russia': '+7',
# #     'Turkey': '+90'
# # }
# # if 'France' in dct:
# #     print('Yes')
# # else:
# #     print('No')
#
# # print(len(dct))
#
# # dct1 = {
# #     'name': 'Ann',
# #     'age': 16
# # }
# # dct3 = dct | dct1
# # print(dct3)
#
# # dct = {
# #      'USA': '+1',
# #      'Russia': '+7',
# #      'Turkey': '+90'
# #     }
# # for key in dct:
# #     print(key)
#
#
# # dct = {
# #      'USA': '+1',
# #      'Russia': '+7',
# #      'Turkey': '+90'
# #     }
# # for value in dct.values():
# #     print(value)
#
# dct = {
#      'USA': '+1',
#      'Russia': '+7',
#      'Turkey': '+90'
#     }
# for key, value in dct.items():
#     print(key, value)
#
# dct = {
#      'USA': '+1',
#      'Russia': '+7',
#      'Turkey': '+90'
#     }
# for key in dct:
#     print(dct[key])
# #
# dct = {
#      'USA': '+1',
#      'Russia': '+7',
#      'Turkey': '+90'
#     }
# print(*dct, sep = '\n')
# dct = {
#      'USA': '+1',
#      'Russia': '+7',
#      'Turkey': '+90'
#     }
# # print(dct.setdefault('France', '+75'))
# # print(dct)
# # print(dct.pop('Turkey'))
# print(dct.popitem())
# print(dct)
dct = {
     'USA': '+1',
     'Russia': '+7',
     'Turkey': '+90'
    }
# keys = list(dct.keys())
# print(keys)
# keys = list(dct.values())
# print(keys)
keys = list(dct.items())
print(keys)
keys = dict(dct.items())
print(keys)
keys = tuple(dct.items())
print(keys)
keys = set(dct.items())
print(keys)
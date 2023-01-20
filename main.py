# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

import os
os.system("clear")

# Задайте последовательность чисел. 
# Напишите программу, которая выведет список чисел кратных 2.

# Старое решение:

# from random import randint

# list_1 = []

# for i in range(1, 10):
#     list_1.append(randint(1, 6))

# print(list_1)

# list_2 = []

# for i in list_1:
#     if i % 2 ==0:
#         list_2.append(i)

# print(list_2)

# Новое решение:

# from random import randint

# list_1 = []
# for i in range(1, 10):
#     list_1.append(randint(1, 6))

# print(list_1)

# new_list = list(filter(lambda x: x % 2 == 0, list_1))
# print(new_list)


# Задайте последовательность чисел. 
# Напишите программу, которая возведет все значения списка в куб.

# Старое решение:

# from random import randint

# list_1 = []

# for i in range(1, 10):
#     list_1.append(randint(1, 6))

# print(list_1)

# list_2 = []

# for i in list_1:
#     list_2.append(i*i*i)

# print(list_2)

# Новое решение:

# from random import randint

# list_1 = []

# for i in range(1, 10):
#     list_1.append(randint(1, 6))

# print(list_1)

# new_list = list(map(lambda x: x*x*x, list_1))

# print(new_list)

# Задайте 3 спика.
# Создайте кортежи из элементов списков.

#Старое решение

# list_1 = [1,2,3]
# list_2 = ["w","e","r"]
# list_3 = ['z','g','h']

# tuple_1 = (list_1[0],list_2[0],list_3[0])
# tuple_2 = (list_1[1],list_2[1],list_3[1])
# tuple_3 = (list_1[2],list_2[2],list_3[2])

# main_tuple = tuple_1 + tuple_2 + tuple_3

# print(main_tuple)

# # Новое решение:
# list_1 = [1,2,3]
# list_2 = ["w","e","r"]
# list_3 = ['z','g','h']
# print(list(zip(list_1, list_2, list_3)))

# Дан список чисел. 
# Используя функцию enumerate() в заголовке цикла for, 
# создайте второй список, в котором каждый элемент должен быть строкой, 
# включающей через пробел индекс и значение соответствующего элемента первого списка.

# list_1 = [23, 34, 5657, 41, 2, 45, 467, 7]
# list_2 = []
# for i in enumerate(list_1):
#     list_2.append(i)
# print(list_2)

#Задайте список чисел от 1 до 5 в квадрате, затем удалите из него четные числа.
# Используйте только list compression

nums = [i*i for i in range(1,6)]
print(nums)
odd_nums = [i for i in nums if i%2 == 1]
print(odd_nums)
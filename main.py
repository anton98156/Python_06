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
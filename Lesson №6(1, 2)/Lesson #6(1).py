# Задание №1
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def prime_numbers(list):
#     count=0
#     for k in list:
#         if(k < 2):
#             continue
#         else:
#             for i in range(2, k):
#                 if(k % i == 0):
#                     break
#             else:
#                 count+=1
#     return count
# print (prime_numbers(list))

# Задание №2
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def delete(data, key):
#     count = data.count(key)
#     for i in range(len(data) -1, -1, -1):
#         if data[i] == key:
#             data.remove(data[i])
#     return count
# delete(list, 5)
# print(list)

# Задание №3
# def delete_number():
#         from random import randint
#         a = []
#         for i in range(4):
#                 c = []
#                 [c.append(randint(-20, 10)) for x in range(4)]
#                 a.append(c)
#         counter = 0
#         for i in a:
#                 for x in i:
#                         if x < 0:
#                                 counter += 1
#         print(counter)
# delete_number()

# Задание №4
# def square():
#         import math
#         print('1 - треугольник''\n'
#               '2 - прямоугольник''\n'
#               '3 - круг')
#         figure = str(input("Выбор фигуры: "))
#         if figure == "1":
#                 a = float(input("Введите сторону a: "))
#                 b = float(input("Введите сторону b: "))
#                 c = float(input("Введите сторону c: "))
#                 p = (a + b + c) / 2
#                 s = math.sqrt((p * ( p - a ) * ( p - b ) * ( p - c )))
#         elif figure == "2":
#                 a = float(input("Введите сторону a: "))
#                 b = float(input("Введите сторону b: "))
#                 s = a * b
#         elif figure == "3":
#                 r = float(input("Введите радиус r: "))
#                 s = math.pi*( r ** 2)
#         print('Площадь равна: ', s)
# square()
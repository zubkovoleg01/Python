# Задание №1
# def divider(a, b):
#     if b == 0:
#         return a
#     else:
#         return divider(b, a % b)
# print(divider(20, 8))

# Задание №2
# from  random import choice
# z = '0123456789'
#
# def rand(out_f:str, z_f:str, count:int):
#     x = choice(z_f)
#     if out_f.find(x) == -1:
#         out_f += x
#         count -= 1
#     if count > 0:
#         return rand(out_f, z_f, count)
#     return out_f
#
# def attempts(number, count):
#     bulls = 0
#     cows = 0
#     b = input('Введите четырехзначное число: ')
#     for i in range(len(number)):
#         if number[i] == b[i]:
#             bulls += 1
#         elif b.find(number[i]) != -1:
#             cows += 1
#     count += 1
#     if bulls == 4:
#         return count
#     else:
#         print(f'Быков: {bulls}, Коров: {cows}')
#         return attempts(number, count)
#
# a = rand('', z, 4)
# print(a)
# print(f'Выше колличество попыток угадать число "{a}" равно: {attempts(a, 0)}')
#
# import random
# a = [random.randint(0, 100) for i in range(30)]
# a.sort()
# def search(mas, index, l, h):
#     x = (l + h) // 2
#     if mas[x] == index:
#         return x
#     elif mas[x] > index:
#         h = x + 1
#         print('mas[x] > index:')
#         return search(mas, index, l, h)
#     elif mas[x] < index:
#         l = x - 1
#         print('mas[x] < index:')
#         return search(mas, index, l, h)


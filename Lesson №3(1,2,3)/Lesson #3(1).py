# Задание 1
# num1 = int(input('Введите начало диапазона: '))
# num2 = int(input('Введите конец диапазона: '))
# for i in range(num1, num2+1):
#     if i % 7 == 0:
#         print(i)

# Задание 2
# num1 = int(input('Введите начало диапазона: '))
# num2 = int(input('Введите конец диапазона: '))
# for i in range(num1, num2):
#     print(i, end=' ')
# print()
#
# for i in range(num2 -1, num1 - 1, -1 ):
#     print(i, end=' ')
# print()
#
# for i in range(num1, num2):
#     if i % 7 == 0:
#         print(i, end=' ')
# print()
#
# for i in range(num1, num2):
#     if i % 5 == 0:
#         print(i, end=' ')

# Задание 3
# num1 = int(input('Введите начало диапазона: '))
# num2 = int(input('Введите конец диапазона: '))

# (Длинное решение)
# for i in range(num1, num2):
#     if i % 3 == 0:
#         i = 'Fizz'
#         print(i, end=' ')
#         print()
# for i in range(num1, num2):
#     if i % 5 == 0:
#         i = 'Buzz'
#         print(i, end=' ')
#         print()
# for i in range(num1, num2):
#     if i % 3 == 0 and i % 5 == 0:
#         i = 'Fizz Buzz'
#         print(i, end=' ')
#         print()
# for i in range(num1, num2):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i, end=' ')
#         print()

# (Короткое решение)
# for i in range(num1, num2):
#     if i % 3 == 0:
#         i = 'Fizz'
#     elif i % 5 == 0:
#         i = 'Buzz'
#     elif i % 3 == 0 and i % 5 == 0:
#         i = 'Fizz Buzz'
#     print(i, end='\n')

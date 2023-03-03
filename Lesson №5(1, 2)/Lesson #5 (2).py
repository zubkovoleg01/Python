# Задание №1
# from random import randint
# weight = 10
# height = 10
# count = []
# matrix = []
# for i in range(weight):
#     row = []
#     for k in range(height):
#         n = int(randint(10, 1000))
#         if 99 < n < 1000:
#             count += [n]
#         row.append(n)
#     matrix.append(row)
# for i in matrix:
#     for k in i:
#         print(k, end='\t')
#     print()
# print('Трехкратные чиcла:', count)
# multiplay = []
# for j in count:
#     summ = 0
#     while n > 0:
#         digit = n % 10
#         summ += digit
#         n = n // 10
#     if summ % 5 == 0:
#         multiplay.append(summ)
# print('Сумма чисел кратных 5:', multiplay)

# Задание №2
# weight = int(input('Введите ширину матрицы: '))
# height = int(input('Введите высоту матрицы: '))
# a = [[0] * height for i in range(weight)]
# for i in range(weight):
#     for k in range(height):
#         a[i][k] = i + k
# for row in a:
#     print('\t'.join([str(elem) for elem in row]))





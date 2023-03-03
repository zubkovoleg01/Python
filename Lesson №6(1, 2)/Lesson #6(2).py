# Задание №1
# import random
# a = 3
# b = 3
# matrix = [[random.randint(1, 20) for i in range(a)] for k in range(b)]
# [print(*row, sep='\t') for row in matrix]
# sum = 0
# while len(matrix[0]):
#     maximal = []
#     for row in matrix:
#         new_max = max(row)
#         row.remove(new_max)
#         maximal.append(new_max)
#     sum += max(maximal)
#     print('__________________________________')
#     [print(*row, sep='\t') for row in matrix]
# print(sum)

# Задание №2
# def get_perimeter(matrix):
#     perimeter = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 1:
#                 if j == 0 or matrix[i][j - 1] == 0:
#                     perimeter += 1
#                 elif j == len(matrix[0]) - 1 or matrix[i][j + 1] == 0:
#                     perimeter += 1
#     return perimeter
# print(get_perimeter([[0, 0, 0],
#                      [0, 1, 0],
#                      [0, 0, 0],]))

# Задание №3
# import random
# def move(matrix, k = 1):
#     a = len(matrix) - 1
#     b = len(matrix[0]) - 1
#     for x in range(k):
#         one = matrix[0][0]
#         for i in range(a -1, -1, -1):
#             for j in range(b -1, -1, -1):
#                 if i == a - 1 and j == b - 1:
#                     matrix[0][0] = matrix[i][j]
#                 elif j == b - 1:
#                     matrix[i + 1][0] = matrix[i][j]
#                 else:
#                     matrix[i][j] = matrix[i][j - 1]
#         matrix[0][1] = one
# matrix = [[random.randint(1, 10) for i in range(5)] for k in range(5)]
# [print(*row, sep='\t') for row in matrix]
# move(matrix)
# print('___________________')
# [print(*row, sep='\t') for row in matrix]
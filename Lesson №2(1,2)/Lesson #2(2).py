# Задание 1
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# even_numbers = odd_numbers = multiples_nine = 0
# for i in range(num1, num2 + 1):
#     if i % 2 == 0:
#         even_numbers += i
#     if i % 2 != 0:
#         odd_numbers += i
#     if i % 9 == 0:
#         multiples_nine += i
# print("Сумма четных: ", even_numbers)
# print("Сумма нечетных: ", odd_numbers)
# print("Сумма кратных 9: ", multiples_nine)

# Если честно, не разобрался со среднеарифмитическим :(

# Задание 2
# line = int(input('Введите длину линии: '))
# symbol = str(input('Введите символ: '))
# for i in range(line):
#     print(symbol)

# Задание 3
# number = 0
# while number != 7:
#     number = float(input("Enter a number ('7' - exit): "))
#     if number > 0:
#         print('Number is positive')
#     elif number < 0:
#         print('Number is negative')
#     elif number == 0:
#         print('Number is equal to zero')
# else:
#     print('Good bye!')

# Задание 4
# enter = float(input("Enter a number ('7' - exit): "))
# sum = max = min = enter
# print(f'SUM: {sum} \n'
#       f'MAX: {max} \n'
#       f'MIN: {min}')
# while enter != 7:
#     enter = float(input("Enter a number ('7' - exit): "))
#     sum = sum + enter
#     if enter > max:
#         max = enter
#     elif enter < min:
#         min = enter
#     print(f'SUM: {sum} \n'
#           f'MAX: {max} \n'
#           f'MIN: {min}')
# print('Good bye!')
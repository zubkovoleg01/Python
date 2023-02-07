# Задание 1
# number = int(input('Введите число от 1 до 100: '))
# if number < 1 or number > 100:
#     print('Ошибка ввода!')
# elif number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)

# Задание 2
# number = int(input('Введите число: '))
# print(number ** 0)
# print(number ** 1)
# print(number ** 2)
# print(number ** 3)
# print(number ** 4)
# print(number ** 5)
# print(number ** 6)
# print(number ** 7)

# Задание 3
# time = int(input('Введите время разговора в минутах: '))
# operator = str(input('Выберите оператора(MTS, Beeline, Tele2, Megafon): '))
# MTS = 5 * time
# Beeline = 6 * time
# Tele2 = 4.7 * time
# Megafon = 4.9 * time
# if operator == 'MTS':
#     print('Ваша цена за звонок составляет: ', MTS, 'рублей')
# elif operator == 'Beeline':
#     print('Ваша цена за звонок составляет: ', Beeline, 'рублей')
# elif operator == 'Tele2':
#     print('Ваша цена за звонок составляет: ', Tele2, 'рублей')
# elif operator == 'Megafon':
#     print('Ваша цена за звонок составляет: ', Megafon, 'рублей')
# else:
#     print('Мы не поддерживаем данного оператора! Повторите снова!')

# Задание 4
# manager1 = int(input('Введите уровень продажи для первого менеджера: '))
# manager2 = int(input('Введите уровень продажи для второго менеджера: '))
# manager3 = int(input('Введите уровень продажи для третьего менеджера: '))
# salary = int(200)
#
# if manager1 > 1000:
#     salary1 = salary + manager1 * 0.08
# else:
#     if manager1 < 500:
#         salary1 = salary + manager1 * 0.03
#     else:
#         salary1 = salary + manager1 * 0.05
# if manager2 > 1000:
#     salary2 = salary + manager2 * 0.08
# else:
#     if manager2 < 500:
#         salary2 = salary + manager2 * 0.03
#     else:
#         salary2 = salary + manager2 * 0.05
# if manager3 > 1000:
#     salary3 = salary + manager3 * 0.08
# else:
#     if manager3 < 500:
#         salary3 = salary + manager3 * 0.03
#     else:
#         salary3 = salary + manager3 * 0.05
# print('Зарплата 1 менеджера: ', salary1)
# print('Зарплата 2 менеджера: ', salary2)
# print('Зарплата 3 менеджера: ', salary3)
#
# if salary1 > salary2 and salary1 > salary3:
#     print('Лучший по уровням продажам - 1 менеджер!')
#     salary1 += 200
# if salary2 > salary1 and salary2 > salary3:
#     print('Лучший по уровням продажам - 2 менеджер!')
#     salary2 += 200
# if salary3 > salary1 and salary3 > salary2:
#     print('Лучший по уровням продажам - 3 менеджер!')
#     salary3 += 200





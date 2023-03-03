# Задача №1
# txt = input(':')
# vowels = lambda x: x if x not in 'ауоыиэяюёе' else ''
# print(''.join(map(vowels, txt)))

# Задача №2
# string = input(':')
# bool = (lambda x: str.isalpha(string))
# print(bool(string))

# Задача №3 
# from functools import reduce
# list_of_numbers = input(':')
# product = reduce((lambda x,y: x*y), list_of_numbers)
# print(product(list_of_numbers))


# Задача №4
# string = input(':')
# palindrome = lambda string: string == string[::-1]
# print(palindrome(string))
#
# # Задача №5
# num = int(input(':'))
# print((lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:]))(num))
#
# # Задача №6
# num = int(input(':'))
# print((lambda b: (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1,b))(num))

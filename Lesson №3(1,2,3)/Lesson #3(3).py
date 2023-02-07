forexit = False
while (forexit != True):
    figure = input('Выберите фигуру а-к (нажмите 0 для выхода): ')
    if (figure == "а"):
        i = 5
        while i >= 1:
            j = 5
            while j > i:
                print(' ', end=' ')
                j -= 1
            k = 1
            while k <= i:
                print('*', end=' ')
                k += 1
            print("\r")
            i -= 1
    elif (figure == "б"):
        for i in range(0, 5):
            for j in range(0, i + 1):
                print("* ", end="")
            print("\r")
    elif (figure == "в"):
        for i in range(5, 1, -1):
            for space in range(0, 5 - i):
                print("  ", end="")
            for j in range(i, 2 * i - 1):
                print("* ", end="")
            for j in range(1, i - 1):
                print("* ", end="")
            print("\r")
    elif (figure == "г"):
        k = 4
        for i in range(0, 5):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i + 1):
                print("* ", end="")
            print("\r")
    elif (figure == "д"):
        i = 0
        while i <= 4:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= 5 - 1:
                print('*', end=' ')
                k += 1
            print()
            i += 1
        i = 4
        while i >= 0:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= 5 - 1:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1
    elif (figure == "е"):
        n = 3
        i = 1
        while (i <= n):
            j = 1
            while (j <= i):
                print("*", end="")
                j += 1
            k = 1
            while (k <= 2 * (n - i)):
                print(" ", end="")
                k += 1
            l = 1
            while (l <= i):
                print("*", end="")
                l += 1
            print()
            i += 1
        i = n - 1
        while (i >= 1):
            j = 1
            while (j <= i):
                print("*", end="")
                j += 1
            k = 1
            while (k <= 2 * (n - i)):
                print(" ", end="")
                k += 1
            l = 1
            while (l <= i):
                print("*", end="")
                l += 1
            print()
            i -= 1
    elif (figure == "ж"):
        for i in range(0, 3):
            for j in range(0, i + 1):
                print("*", end=' ')
            print(" ")
        for i in range(3, 0, -1):
            for j in range(0, i - 1):
                print("*", end=' ')
            print(" ")
    elif (figure == "з"):
        rows = 3
        i = 1
        while i <= rows:
            j = i
            while j < rows:
                print(' ', end=' ')
                j += 1
            k = 1
            while k <= i:
                print('*', end=' ')
                k += 1
            print()
            i += 1
        i = rows
        while i >= 1:
            j = i
            while j <= rows:
                print(' ', end=' ')
                j += 1
            k = 1
            while k < i:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1
    elif (figure == "и"):
        for i in range(5, 0, -1):
            for j in range(0, i):
                print("* ", end="")
            print("\r")
    elif (figure == "к"):
        k = 2 * 5 - 2
        for i in range(0, 5):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i + 1):
                print("* ", end="")
            print("\r")
    elif (figure == "0"):
        forexit = True
    else:
        print("Неправильный ввод! Повторите попытку: \n")
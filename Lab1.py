import math             # Импорт библиотек
import numpy as np

A = int(input("Enter point start "))   # Ввод чисел
B = int(input("Enter point end "))
H = float(input("Enter step "))
M = int(input('enter an integert to start the segment '))
N = int(input('enter an intgert to end the segment '))


def level_a():                                                  # Объявдение функции
    count = 0                                                   # Счетчик
    for x in np.arange(A, B, H):                            # Цикл перебора
        f = x * math.exp(x) + 2 * math.sin(x) - \
            math.sqrt(math.fabs(x ** 3 - x ** 2))               # Функция
        print('f = {0:.4f}   -->   x = {1:.1f}'.format(f, x))   # Вывод ответа
        if M <= f <= N:                                         # Условие промежутка
            count += 1                                          # Счетчик + 1
    print(count)


if __name__ == '__main__':                                      # Старт программы
    level_a()

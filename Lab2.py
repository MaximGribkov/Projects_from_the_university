# Лабораторная 2 из списка

import math
import numpy as np


def level_a():
    count_point_in_area = 0
    summ = 0
    count = 0
    count_point = int(input('Enter num point '))
    start = int(input("Enter start poin "))
    end = int(input("Enter end point "))
    step = (end - start) / (count_point - 1)  # Нахождение шага
    for x in np.arange(start, end + 1, step):   # Цикл нахождения х и у с помощью шага
        y = x * math.exp(x) + 2 * math.sin(x) - \
            math.sqrt(math.fabs(x ** 3 - x ** 2))
        count += 1
        summ += y
        if (y > -10) and (y < 4):   # Услсовный прямоугольник
            if (x > -6) and (x < 5):
                count_point_in_area += 1
                print('This point is included in the segment y = {0:.4f}, '
                      'x = {1}'.format(y, x))
        print('y = {0:.4f}   -->   x = {1:.1f}'.format(y, x))

    sr = summ / count       # Среднее арифмитическое
    print('Count point {}'.format(count))
    print('Sum {}'.format(summ))
    print('Mean {:.4f}'.format(sr))
    print('Num point in area = {}'.format(count_point_in_area))


if __name__ == '__main__':
    level_a()

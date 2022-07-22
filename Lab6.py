import random
import math

A = int(input('Enter the beginning of the range '))
B = int(input('Enter the end of the range '))

num = []
for i in range(A, B + 1):
    num.append(random.randint(A, B))
num.sort()  # Сортировка списка от меньшего к большему
print('First list {}'.format(num))


def print_min_max():
    print('min = {}'.format(num[0]))  # Вывод мнимального значения
    last_element = len(num) - 1  # Нахождение последжнего индекса списка
    print('max = {}'.format(num[last_element]))  # Вывод максимального значения


def level_a():
    min_num = math.fabs(num[0])  # Нахождение минимального числа в списке
    new_num = [x if x % 2 == 0 else int(min_num) for x in num]  # лист компрехендшнс, заполнение нового списка
    # Замена не четных числе на минимальное число
    print('New list {}'.format(new_num))


if __name__ == '__main__':
    print_min_max()
    level_a()

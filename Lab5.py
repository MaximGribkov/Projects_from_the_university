import random

A = int(input('Enter the beginning of the range '))
B = int(input('Enter the end of the range '))

num = []
for i in range(A, B + 1):             # Заполнение списка рандомными числами
    num.append(random.randint(A, B))  # в выбранномом диапазоне
print(num)


def level_a():
    count = 0
    summ = 0
    for x in num:
        if x % 2 == 0:          # Проверка на четность
            count += 1          # Количество четных чисел
            summ += x           # Сумма четный числе
            print('x = {0} <--> count = {1} <--> sum = {2}'.format(
                x, count, summ))        # Вывод всех чисел
            sr = summ / count       # Среднее число
    print('mean = {}'.format(sr))   # Вывод числа


if __name__ == '__main__':
    level_a()

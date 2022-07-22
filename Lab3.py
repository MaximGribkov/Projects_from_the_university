n = int(input("Enter the number of point "))


def level_a():
    summ_list = []                                  # Создание списка
    for i in range(n):                              # Цикл
        a = n/((n ** 3) + 1)                        # Функция
        summ_list.append(a)                         # Добавление в конец списка числа
    print("Sum = {:.4}".format(sum(summ_list)))     # Вывод


if __name__ == '__main__':
    level_a()

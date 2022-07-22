# Лабораторная 4 из списка


a = int(input('enter a '))


minn = 0
maxx = 0
reterned = []
while a != 0:
    if maxx == 0:                           # Проверка первывй ли это элемент
        maxx = a
        minn = a
    else:
        if a < minn:                        # Переприсвоение минимумаб максимума
            minn = a
        if a > maxx:
            maxx = a
    print('min = {0}  <-->  max = {1}'
          .format(minn, maxx))              # Ответ
    a = int(input('enter a '))
    reterned.append(minn)                   # Добавление в список для дальнейшего вывода сортировки
reterned.sort()                             # Сортировка от наименьшего к наибольшему
sortedd = []                                # Новый список для удаления дублей
for i in reterned:                          # Цикл для удаление дублей
    if i not in sortedd:
        sortedd.append(i)                   # Добавление в новый список

print('All min num in reverse order {}'.format(sortedd))

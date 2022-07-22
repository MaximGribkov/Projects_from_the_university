string = input('Enter string ')


# aa_99.dd,ff;gg:qq\n88\tyy!rr?77 пример строки


def enumeration():
    num = []                                   # Новый список
    symbol = ''                                # Пустая строка
    for char in string:                        # Перебор всех символов в строке
        if '0' <= char <= '9':                 # Сравнение по коду ASKII
            symbol += char                     # Добавление к символам
        else:
            if symbol != '':                   # Проверка путая ли строка, елси нет, то добавляем в список
                num.append(int(symbol))        # Добавление в список и привидение к типу int
                symbol = ''                    # Обнуляем строку
    if symbol != '':                           # Цикл for не включает в себя последний символ строки string,
        num.append(int(symbol))                # для корректной работы вводится дополнительная проверка
    print('Separated numbers {}'.format(num))  # остались ли символы в строке symbol


if __name__ == '__main__':
    enumeration()

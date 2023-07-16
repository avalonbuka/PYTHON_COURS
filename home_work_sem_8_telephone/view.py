def input_num():
    ask = int(input("Выбери действие:\n1 - Записать нового пользователя\n2 - Найти пользователя "
                    "\n3 - Изменить пользователя \n4 - Удалить пользователя \n5 - Отсортировать"
                    "\n6 - Вывести всех пользователей\n7 - Выйти\n"))
    return ask


def input_name():
    id = input("Введите id - ")
    name = input("Введите ФИО - ")
    tele = input("Введите телефон - ")
    res = id + "|" + name + "|" + tele + "\n"
    return res


def input_char():
    char = input("Введите характеристику - ")
    return char


def select_number():
    num = int(input("Ввыберите строку - "))
    return num


def select_sort():
    num = int(input(
        "1 - Сортировка по id\n2 - Сортировка по ФИО \n3 - Сортировка по телефону\n"))
    return num

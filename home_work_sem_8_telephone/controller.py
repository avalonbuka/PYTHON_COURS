from database import *
from view import *


def main():
    while True:
        num = input_num()
        if num == 1:
            res = input_name()
            write_name(res)
            print("Успешно записано!\n")
        elif num == 2:
            char = input_char()
            search_data(char)
            print("Успешно найдено!\n")
        elif num == 3:
            char = input_char()
            lst_find_man = search_data(char)
            sel_num = select_number()
            new_man = input_name()
            change_data(lst_find_man[sel_num-1], new_man)
            print("Успешно Изменено!\n")
        elif num == 4:
            char = input_char()
            lst_find_man = search_data(char)
            sel_num = select_number()
            delete_data(lst_find_man[sel_num-1])
            print("Успешно удалено!\n")
        elif num == 5:
            sort_num = select_sort()
            sort(sort_num)
            print("Успешно отсортировано!\n")
        elif num == 6:
            view_all()
        elif num == 7:
            print("Вы вышли из программы!\n")
            return


main()

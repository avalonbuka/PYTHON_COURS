def write_name(name):
    with open("telephone.txt", "a", encoding="UTF-8") as file:
        file.write(name)


def search_data(char):
    count = 0
    lst_find_man = []
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            if char in row:
                count += 1
                print(f"{count}) {row.strip()}")
                lst_find_man.append(row)

    return lst_find_man


def change_data(old_data, new_data):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()

    with open("telephone.txt", "w", encoding="UTF-8") as file:
        for row in lst:
            if row == old_data:
                file.write(new_data)
            else:
                file.write(row)


def delete_data(old_data):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()

    with open("telephone.txt", "w", encoding="UTF-8") as file:
        for row in lst:
            if row == old_data:
                continue
            else:
                file.write(row)


def sort(num):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
    if num == 2:
        lst.sort(key=lambda x: x.split("|")[1])
    else:
        lst.sort(key=lambda x: int(x.split("|")[num-1]))

    with open("telephone.txt", "w", encoding="UTF-8") as file:
        file.writelines(lst)


def view_all():
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        print(file.read())

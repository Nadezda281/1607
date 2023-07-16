def input_num():
    ask = int(input("1 - Добавить пользователя\n2 - Найти пользователя\n3 - Изменить пользователя\n4 - Удалить пользователя\n5 - Остортировать пользователя\n6 -Вывести все\n7 -Выйти\n"))
    return ask

def input_info():
    fio = input("Введи ФИО человека - ")
    birth = input("Введи дату рождения - ")
    tele = input("Введи телефон - ")
    info = f"{fio},{birth},{tele}\n"
    return info

def input_char():
    char = input("Введите характеристику - ")
    return char

def select_num():
    num=int(input("Выбери строчку - "))
    return num

def select_sort():
    sort_num = int(input("1 - Отсортировать по ФИО\n2 - Отсортировать по дате рождения\n3 - Отсортировать по телефону\n"))
    return sort_num

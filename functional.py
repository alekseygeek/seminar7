def get_contact():
    # получение строки который записываем в файл
    surname = input('введите фамилию:')
    name = input('введите имя: ')
    phone = input("введите номер телефона: ")
    description = input('описание: ')
    return f'фамилия:{surname}, имя: {name}, телефон:{phone}, комментарии:{description}\n'


def fin_contact(book: list, req: str) -> str:
    a = ''
    for i in book:
        if i.find(req) != -1:
            a = i
    if a == '':
        return "нет такого контакта !"
    else:
        return a


def get_request():
    return input('найти контакт: ')


def choose_mode():
    return int(input("записать  контакт (жми)- 1 \nнайти контакт (жми) - 2\nвыход (жми)- 3 \nнажмите цифру 1,2,3: "))

def get_contact():
    # получение строки который записываем в файл
    surname = input('введите фамилию:')
    name = input('введите имя: ')
    phone = input("введите номер телефона: ")
    description = input('описание: ')
    return f'{surname} {name} {phone} {description}\n'


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
    return int(input("записать  контакт - 1 \nнайти контакт - 2\nвыход - 3 \nнажмите 1,2,3: "))

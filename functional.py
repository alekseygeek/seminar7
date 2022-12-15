def get_contact():
    # получение строки который записываем в файл
    name = input(' введите имя: ')
    phone = input("введите номер телефона: ")
    return f'{name} , {phone} \n'


def fin_contact(book: list, req: str) -> str:
    a = ''
    for i in book:
        if i.find(req) != -1:
            a = i
    if a == '':
        return "Empty(пустой)"
    else:
        return a


def get_request():
    return input('найти контакт: ')


def choose_mode():
    return int(input("записать  контакт - 1 \nнайти контакт - 2\nвыход - 3 \nнажмите 1,2,3: "))

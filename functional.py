def get_contact() -> dict:

    surname = input('введите фамилию:')
    name = input('введите имя: ')
    phone = input("введите номер телефона: ")
    description = input('описание: ')
    return {'surname': surname, 'name': name, 'phone': phone, 'description': description}


def fin_contact(book: list, req: str) -> str:
    a = ''
    for i in book:
        if i.find(req) != -1:
            a = i
    if a == '':
        return "нет такого контакта !"
    else:
        return a


def get_request() -> str:
    return input('найти контакт: ')


def choose_mode() -> int:
    print()
    return int(input("записать  контакт (жми)- 1 \nнайти контакт (жми) - 2\nвыход (жми)- 3 \nнажмите цифру 1,2,3: "))

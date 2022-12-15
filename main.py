import functional as fun
import log as l


while True:
    mode = fun.choose_mode()
    if mode == 1:
        l.write_new(fun.get_contact())
    elif mode == 2:
        contact = fun.get_request()
        book = l.get_book()
        print(fun.fin_contact(book, contact))
    elif mode == 3:
        print('вы вышли из программы')
        break
    else:
        print('такого режима нет !!!')

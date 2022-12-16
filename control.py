import functional as fun
import log


def main():

    log.prepare_files()

    while True:
        mode = fun.choose_mode()
        if mode == 1:
            log.write_new(fun.get_contact())
        elif mode == 2:
            contact = fun.get_request()
            book = log.get_book()
            print(fun.fin_contact(book, contact))
        elif mode == 3:
            print('вы вышли из программы')
            break
        else:
            print('такого режима нет !!!')

import csv
import os

FIELDNAMES = ['surname', 'name', 'phone', 'description']


def write_text(contact):
    line = 'фамилия:{surname}, имя: {name}, телефон:{phone}, комментарии:{description}\n'.format(
        **contact)
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(line)


def get_book():
    book = []
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
            book.append(line)
    return book


def write_csv(contact):
    with open('book1.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(contact)


def write_new(contact):
    write_text(contact)
    write_csv(contact)


def prepare_files():
    if not os.path.exists('book.txt'):
        fd = open('book.txt', 'w')
        fd.close()
    if not os.path.exists('book1.csv'):
        with open('book1.csv', 'a+', encoding='utf-8',newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

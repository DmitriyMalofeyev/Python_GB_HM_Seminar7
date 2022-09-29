from pyexpat import model

from HW.function import inbox_contact, export_box, import_tel


def start():
    while True:
        var = input('Добро пожаловать в телефонный справочник! Введите \n1-чтобы внести новый контакт\n'
                '2-чтобы экспортировать данные \n'
                '3-чтобы выйти \n')

        if var == '1':
            fio = input("Введите ФИО через пробел: ")
            tel_number = input("Введите номер телефона : ")
            inbox_contact(fio, tel_number)
            print('Данные сохранены в data_tel.txt\n')
        if var == '2':
            tel_list = import_tel()
            export_box(tel_list)
            print('Данные экспортированы \n')
        if var == '3':
            break

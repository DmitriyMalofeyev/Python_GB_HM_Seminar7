def inbox_contact(fio, tel_number):
    with open('data_tel.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{fio} * {tel_number}\n')


def export_box(tel_list):
    tel_list = [i.replace('*', '') for i in tel_list]
    with open('export_box.csv', 'w+', encoding='UTF-8') as csv:
        for i in range(len(tel_list)):
            csv.write(f'{i + 1}. {tel_list[i]}')


def import_tel(showfile='data_tel.txt'):
    with open(showfile, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        file.close()
        return lines




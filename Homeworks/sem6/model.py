import view
import checknum


def check_dict(a):
    return list(a.items())


def read_txt():
    lst = ''
    with open('phones_numbers.txt', 'r') as data:
        lst = data.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].replace(' \n', '')
    return lst


def write_txt(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].split(': ')
    with open('phones_numbers.txt', 'w') as data:
        for i in range(len(lst)):
            data.write(lst[i][0]+': '+lst[i][1]+' \n')
    with open('phones_numbers_mod1.txt', 'w') as data:
        for i in range(len(lst)):
            data.write(lst[i][1] + ' ;' + lst[i][0] + ' \n')
    with open('phones_numbers_mod2.txt', 'w') as data:
        for i in range(len(lst)):
            data.write(lst[i][0] + ' - ' + lst[i][1] + ' \n')


def en_list(lst):
    a = list(enumerate(lst, start=1))
    b = ''
    for i in range(len(a)):
        b = b + str(a[i][0]) + '.' + a[i][1] + ' \n'
    return b


def input_new_contact(lst):
    FIO = view.get_info('Input FIO: ')
    ph_number = str(checknum.check_num('Input phone number: '))
    lst.append(FIO + ': ' + ph_number)
    write_txt(lst)


def change_name_or_number(lst):
    b = checknum.check_min_max(f'Choose position: ', 1, len(lst)) - 1
    c = 0
    while c != 3:
        c = checknum.check_min_max(
            'Change:\n1.Number\n\
2.Name\n\
3.Back\n\
Choose mode: ', 1, 3)
        if c == 1:
            new_number = checknum.check_num('Input new number: ')
            lst[b] = lst[b].split(': ')[0] + ': ' + str(new_number)
            write_txt(lst)
        if c == 2:
            new_name = view.get_info('Input new name: ')
            lst[b] = new_name + ': ' + lst[b].split(': ')[1]
            write_txt(lst)


def delete_position(lst):
    b = checknum.check_min_max(f'Choose position to delete: ', 1, len(lst)) - 1
    lst.pop(b)
    write_txt(lst)


def searc_pos(lst):
    search_lst = []
    search = view.get_info('Input number or name: ')
    for i in range(len(lst)):
        if search.lower() in lst[i].lower():
            search_lst.append(lst[i])
    if len(search_lst) == 0:
        view.show_info('Nothing found')
    else:
        return search_lst

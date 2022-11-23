import tkinter as tk
import model


def search_num(line):
    search_lst = []
    find_option = line
    lst = model.read_txt()
    for i in range(len(lst)):
        if find_option.lower() in lst[i].lower():
            search_lst.append(lst[i])
    if len(search_lst) == 0:
        lbl_show_book['text']='Nothing found'
    else:
        lbl_show_book['text']=model.en_list(search_lst)


def delete_position():
    def confirm_add(pos):
        lst = model.read_txt()
        lst.pop(pos-1)
        model.write_txt(lst)

    mini_window = tk.Tk()
    mini_window.title('Delete number')

    lbl_pos_of_num = tk.Label(
        master=mini_window, text='Input position of number:')
    ent_pos_of_num = tk.Entry(width=40, master=mini_window)
    btn_confirm = tk.Button(master=mini_window, text='Confirm',
                            command=lambda: [confirm_add(int(ent_pos_of_num.get())), mini_window.destroy()])
    btn_cancel = tk.Button(
        master=mini_window, text='Cancel', command=mini_window.destroy)
    lbl_pos_of_num.grid(row=0, column=0)
    ent_pos_of_num.grid(row=0, column=1)
    btn_confirm.grid(row=1, column=0)
    btn_cancel.grid(row=1, column=1)


def change_info():
    def confirm(pos):
        def confirm_add(fio, number):
            lst[pos-1] = fio + ': ' + number
            model.write_txt(lst)

        lst = model.read_txt()
        mini_window = tk.Tk()
        mini_window.title('Input information')

        lbl_fio = tk.Label(master=mini_window, text='FIO:')
        lbl_number = tk.Label(master=mini_window, text='Phone number:')
        ent_fio = tk.Entry(width=40, master=mini_window)
        ent_fio.insert(0, str(lst[pos-1].split(': ')[0]))
        ent_number = tk.Entry(width=40, master=mini_window)
        ent_number.insert(0, str(lst[pos-1].split(': ')[1]))
        btn_confirm = tk.Button(master=mini_window, text='Confirm',
                                command=lambda: [confirm_add(ent_fio.get(), ent_number.get()), mini_window.destroy()])
        btn_cancel = tk.Button(
            master=mini_window, text='Cancel', command=mini_window.destroy)

        lbl_fio.grid(row=0, column=0)
        lbl_number.grid(row=1, column=0)
        ent_fio.grid(row=0, column=1)
        ent_number.grid(row=1, column=1)
        btn_confirm.grid(row=2, column=0)
        btn_cancel.grid(row=2, column=1)

    mini_window = tk.Tk()
    mini_window.title('Position of number')

    lbl_pos_of_num = tk.Label(
        master=mini_window, text='Input position of number:')
    ent_pos_of_num = tk.Entry(width=40, master=mini_window)
    btn_confirm = tk.Button(master=mini_window, text='Confirm',
                            command=lambda: [confirm(int(ent_pos_of_num.get())), mini_window.destroy()])
    btn_cancel = tk.Button(
        master=mini_window, text='Cancel', command=mini_window.destroy)
    lbl_pos_of_num.grid(row=0, column=0)
    ent_pos_of_num.grid(row=0, column=1)
    btn_confirm.grid(row=1, column=0)
    btn_cancel.grid(row=1, column=1)


def add_new_contact():
    def confirm_add(fio, number):
        lst = model.read_txt()
        lst.append(fio + ': ' + number)
        model.write_txt(lst)

    mini_window = tk.Tk()
    mini_window.title('Input information')

    lbl_fio = tk.Label(master=mini_window, text='FIO:')
    lbl_number = tk.Label(master=mini_window, text='Phone number:')
    ent_fio = tk.Entry(width=40, master=mini_window)
    ent_number = tk.Entry(width=40, master=mini_window)
    btn_confirm = tk.Button(master=mini_window, text='Confirm',
                            command=lambda: [confirm_add(ent_fio.get(), ent_number.get()), mini_window.destroy()])
    btn_cancel = tk.Button(
        master=mini_window, text='Cancel', command=mini_window.destroy)

    lbl_fio.grid(row=0, column=0)
    lbl_number.grid(row=1, column=0)
    ent_fio.grid(row=0, column=1)
    ent_number.grid(row=1, column=1)
    btn_confirm.grid(row=2, column=0)
    btn_cancel.grid(row=2, column=1)


def main_window():
    global lbl_show_book
    window_main = tk.Tk()
    window_main.title('Phone book')
    window_main.resizable(width=False, height=False)

    frm_spaces = tk.Frame(master=window_main)
    ent_search = tk.Entry(master=frm_spaces, width=40)
    lbl_show_book = tk.Label(master= frm_spaces, height=11,
                            width=40,bg='white',text=model.en_list(model.read_txt()))
    frm_buttons = tk.Frame(master=window_main)
    btn_search = tk.Button(
        master=frm_buttons, text='Search number', command = lambda: search_num(ent_search.get()))
    btn_add_number = tk.Button(
        master=frm_buttons, text='Add number', command=add_new_contact)
    btn_change = tk.Button(
        master=frm_buttons, text='Change number or name', command=change_info)
    btn_delete = tk.Button(
        master=frm_buttons, text='Delete number', command=delete_position)
    btn_exit = tk.Button(master=frm_buttons, text='Exit',
                        command=window_main.destroy)

    frm_buttons.grid(row=0, column=0)
    btn_search.grid(row=0, column=0, sticky='we', pady=10, padx=5)
    btn_add_number.grid(row=1, column=0, sticky='we', pady=10, padx=5)
    btn_change.grid(row=2, column=0, sticky='we', pady=10, padx=5)
    btn_delete.grid(row=3, column=0, sticky='we', pady=10, padx=5)
    btn_exit.grid(row=4, column=0, sticky='we', pady=10, padx=5)

    frm_spaces.grid(row=0, column=1)
    ent_search.grid(row=0, column=0, sticky='w', padx=5, pady=10,)
    lbl_show_book.grid(row=1, column=0, pady=10, sticky='w')

    window_main.mainloop()

import tkinter as tk
import model


def search_num(line):
    lbl_show_book['text'] = model.search_in_bd(line)


def delete_position():

    mini_window = tk.Tk()
    mini_window.title('Delete number')

    lbl_pos_of_num = tk.Label(master=mini_window,
                              text='Input position of number:')
    ent_pos_of_num = tk.Entry(width=40,
                              master=mini_window)
    btn_confirm = tk.Button(master=mini_window,
                            text='Confirm',
                            command=lambda: [model.delete_from_bd(int(ent_pos_of_num.get())), mini_window.destroy(),label_show_book()])
    btn_cancel = tk.Button(master=mini_window,
                           text='Cancel',
                           command=mini_window.destroy)
    lbl_pos_of_num.grid(row=0,
                        column=0)
    ent_pos_of_num.grid(row=0,
                        column=1)
    btn_confirm.grid(row=1,
                     column=0)
    btn_cancel.grid(row=1,
                    column=1)


def change_info():
    def confirm(pos):
        mini_window = tk.Tk()
        mini_window.title('Input information')
        text_fio = 'FIO'
        text_number = 'number'
        lbl_fio = tk.Label(master=mini_window,
                           text=f'{text_fio}:')
        lbl_number = tk.Label(master=mini_window,
                              text=f'Phone {text_number}:')
        ent_fio = tk.Entry(width=40,
                           master=mini_window)
        ent_fio.insert(0, str(model.find_position(text_fio, pos)))
        ent_number = tk.Entry(width=40,
                              master=mini_window)
        ent_number.insert(0, str(model.find_position(text_number, pos)))
        btn_confirm = tk.Button(master=mini_window,
                                text='Confirm',
                                command=lambda: [model.update_bd(ent_fio.get(), ent_number.get(), pos), mini_window.destroy(),label_show_book()])
        btn_cancel = tk.Button(master=mini_window,
                               text='Cancel',
                               command=mini_window.destroy)

        lbl_fio.grid(row=0,
                     column=0)
        lbl_number.grid(row=1,
                        column=0)
        ent_fio.grid(row=0,
                     column=1)
        ent_number.grid(row=1,
                        column=1)
        btn_confirm.grid(row=2,
                         column=0)
        btn_cancel.grid(row=2,
                        column=1)

    mini_window = tk.Tk()
    mini_window.title('Position of number')

    lbl_pos_of_num = tk.Label(
        master=mini_window, text='Input position of number:')
    ent_pos_of_num = tk.Entry(width=40,
                              master=mini_window)
    btn_confirm = tk.Button(master=mini_window,
                            text='Confirm',
                            command=lambda: [confirm(int(ent_pos_of_num.get())), mini_window.destroy()])
    btn_cancel = tk.Button(master=mini_window,
                           text='Cancel',
                           command=mini_window.destroy)
    lbl_pos_of_num.grid(row=0,
                        column=0)
    ent_pos_of_num.grid(row=0,
                        column=1)
    btn_confirm.grid(row=1,
                     column=0)
    btn_cancel.grid(row=1,
                    column=1)


def add_new_contact():
    mini_window = tk.Tk()
    mini_window.title('Input information')

    lbl_fio = tk.Label(master=mini_window,
                       text='FIO:')
    lbl_number = tk.Label(master=mini_window,
                          text='Phone number:')
    ent_fio = tk.Entry(width=40,
                       master=mini_window)
    ent_number = tk.Entry(width=40,
                          master=mini_window)
    btn_confirm = tk.Button(master=mini_window,
                            text='Confirm',
                            command=lambda: [model.add_contact_to_bd(ent_fio.get(), ent_number.get()), mini_window.destroy(), label_show_book()])
    btn_cancel = tk.Button(master=mini_window,
                           text='Cancel',
                           command=mini_window.destroy)

    lbl_fio.grid(row=0,
                 column=0)
    lbl_number.grid(row=1,
                    column=0)
    ent_fio.grid(row=0,
                 column=1)
    ent_number.grid(row=1,
                    column=1)
    btn_confirm.grid(row=2,
                     column=0)
    btn_cancel.grid(row=2,
                    column=1)

def label_show_book():
    lbl_show_book['text'] = model.show_bd()
    

def main_window():
    global lbl_show_book
    window_main = tk.Tk()
    window_main.title('Phone book')
    window_main.resizable(width=False, height=False)

    frm_spaces = tk.Frame(master=window_main)
    ent_search = tk.Entry(master=frm_spaces,
                          width=40)
    lbl_show_book = tk.Label(master=frm_spaces,
                             height=11,
                             width=40,
                             bg='white',
                             text=model.show_bd())
    frm_buttons = tk.Frame(master=window_main)
    btn_search = tk.Button(master=frm_buttons,
                           text='Search number',
                           command=lambda: search_num(ent_search.get()))
    btn_add_number = tk.Button(master=frm_buttons,
                               text='Add number',
                               command=add_new_contact)
    btn_change = tk.Button(master=frm_buttons,
                           text='Change number or name',
                           command=change_info)
    btn_delete = tk.Button(master=frm_buttons,
                           text='Delete number',
                           command=delete_position)
    btn_exit = tk.Button(master=frm_buttons,
                         text='Exit',
                         command=window_main.destroy)

    frm_buttons.grid(row=0,
                     column=0)
    btn_search.grid(row=0,
                    column=0,
                    sticky='we',
                    pady=10,
                    padx=5)
    btn_add_number.grid(row=1,
                        column=0,
                        sticky='we',
                        pady=10,
                        padx=5)
    btn_change.grid(row=2,
                    column=0,
                    sticky='we',
                    pady=10,
                    padx=5)
    btn_delete.grid(row=3,
                    column=0,
                    sticky='we',
                    pady=10,
                    padx=5)
    btn_exit.grid(row=4,
                  column=0,
                  sticky='we',
                  pady=10,
                  padx=5)

    frm_spaces.grid(row=0,
                    column=1)
    ent_search.grid(row=0,
                    column=0,
                    sticky='w',
                    padx=5,
                    pady=10)
    lbl_show_book.grid(row=1,
                       column=0,
                       pady=10,
                       sticky='w')

    window_main.mainloop()

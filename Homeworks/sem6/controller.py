import model
import view
import checknum
import view_tk


def start():
    view.show_info("Welcome to phone book")
    mod = checknum.check_min_max('Choose mode:\n'
                                 '1.Terminal\n'
                                 '2.Tkinter\n',
                                 1, 2)
    if mod == 1:
        a = 0
        while a != 6:
            a = checknum.check_min_max('1.Show book\n'
                                       '2.Input new number\n'
                                       '3.Search contact\n'
                                       '4.Change number or name\n'
                                       '5.Delete number\n'
                                       '6.Exit\n'
                                       'Choose mode: ', 1, 6)
            if (a == 1) or (a == 4) or (a == 5):
                view.show_info(model.show_bd())
                if a == 4:
                    pos = view.get_info('Input position of contact: ')
                    fio = view.get_info('Input new FIO of contact: ')
                    number = view.get_info('Input new number of contact: ')
                    model.update_bd(fio, number, pos)
                if a == 5:
                    model.delete_from_bd(view.get_info('Input position of contact: '))
            if a == 2:
                name = view.get_info('Input FIO: ')
                numb = view.get_info('Input number: ')
                model.add_contact_to_bd(name, numb)
                view.show_info(model.show_bd())
            if a == 3:
                view.show_info(model.search_in_bd(
                    view.get_info('Input some info: ')))
    if mod == 2:
        view_tk.main_window()

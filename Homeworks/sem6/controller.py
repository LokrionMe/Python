import model
import view
import checknum


def start():
    a = 0
    view.show_info("Welcome to phone book")
    while a != 6:
        lst_of_book = model.read_txt()
        a = checknum.check_min_max(
            '1.Show book\n\
2.Input new number\n\
3.Search contact\n\
4.Change number or name\n\
5.Delete number\n\
6.Exit\n\
Choose mode: ',1, 6)
        if a == 1:
            view.show_info(lst_of_book)
        if a == 2:
            model.input_new_contact(lst_of_book)
        if a == 3:
            serch_lst = model.searc_pos(lst_of_book)
            view.show_info(model.en_list(serch_lst))
        if a == 4:
            view.show_info(model.en_list(lst_of_book))
            model.change_name_or_number(lst_of_book)
        if a == 5:
            view.show_info(model.en_list(lst_of_book))
            model.delete_position(lst_of_book)

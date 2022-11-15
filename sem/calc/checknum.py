import view
def check_num(a):
    while True:
        try:
            num_init = int(view.get_numb(a))
        except ValueError:
            print("It's must be number")
        else:
            return num_init

import view
def check_num(text):
    while True:
        try:
            num_init = int(view.get_info(text))
        except ValueError:
            print("It's must be number")
        else:
            return num_init

def check_min_max(text,min_val,max_val):
    while True:
        try:
            num_init = int(view.get_info(text))
        except ValueError:
            print("It's must be number")
        else:
            if min_val <= num_init <= max_val:
                return num_init
                break
            print(f'Number must be from {min_val} to {max_val}')

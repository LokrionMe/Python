import model
import view
import checknum
import operation

def start():
    view.show_info('Welcome to calculator!')
    a = checknum.check_num('Input int numb: ')
    b = checknum.check_num('Input int numb: ')
    model.init(a,b)
    op = operation.choose_op()
    result = op[0]()
    view.show_info(f'{a} {op[1]} {b} = {result}')
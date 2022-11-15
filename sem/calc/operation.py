import view
import model
def choose_op():
    op_dict = {'+': model.summa,'-': model.raznost,'*':model.dif,'/':model.div,'**':model.pov}
    while True:
        try:
            val = view.get_numb('Choose operation: [+ - * / **] ')
            op = op_dict[val]
        except KeyError:
            print("Choose from list")
        else:
            lst = [op,val]
            return lst
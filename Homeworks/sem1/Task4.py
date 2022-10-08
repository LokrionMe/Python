# Напишите программу,
# которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Input number of quarter from 1 to 4: '))
if a == 1:
    print('x>0 and y>0')
if a == 2:
    print('x<0 and y>0')
if a == 3:
    print('x<0 and y<0')
if a == 4:
    print('x>0 and y<0')
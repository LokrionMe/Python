# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def input_number():
    return input('Input number: ')
a = int(input_number())
print(list(i for i in range(-a, a+1)))
def input_number():
    return input('Input number: ')

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

b = str(input_number())
for i in range(0, len(b)):
    if b[i] == ',':
        print(b[i+1])
        break
    if i == len(b)-1:
        print('no')
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
def input_number():
    return input('Input number: ')


def one_dot(a):
    if a % 1 == 0:
        return 'no'
    else:
        return str(a % 1)[2]


b = input_number()
print(one_dot(float(b)))
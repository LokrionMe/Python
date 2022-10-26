# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
def input_number():
    return input('Input number: ')
print(list((-3)**i for i in range(int(input_number()))))
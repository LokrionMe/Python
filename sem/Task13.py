# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import random
a = int(input('Input number: '))
int_numbers = []
with open('file.txt', 'w') as data:
    for i in range(30):
        int_numbers.append(random.randint(-100, 100))
        data.writelines(str(int_numbers[i]) + ' ')
    data.write('\n')
    data.write(str(a) + '\n')
    for i in range(len(int_numbers)):
        if a==int_numbers[i]:
            data.write('Number founded\n')
            break
        if i == len(int_numbers)-1:
            data.write("Number isn't founded\n")
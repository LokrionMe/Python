# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
def input_number():
    return input('Input number: ')
import random
a = input_number()
int_numbers = [str(random.randint(-100, 100)) for i in range(100)]
print(int_numbers)
for i in range(len(int_numbers)):
    if a in int_numbers[i]:
        print(i, end=' ')

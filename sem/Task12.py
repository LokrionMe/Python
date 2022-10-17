# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from random import shuffle


int_numbers = []
for i in range (10):
    int_numbers.append(i)
print(int_numbers)
shuffle(int_numbers)
print(int_numbers)

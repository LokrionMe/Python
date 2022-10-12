# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

import random

N = int(input('Input integer number: '))
for i in range(N):
    a = random.randint(-100, 100)
    print(a, end=' ')
print()
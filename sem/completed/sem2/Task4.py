#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

import random

a = int(input('Input integer number: '))
spisok_random = [random.randint(-a, a) for i in range(a)]
print(spisok_random)
b = list(map(int, input('Input position with space: ').split()))
print(b)
c = 1
for i in range(len(b)):
    if b[i] < len(spisok_random):
        c *= spisok_random[b[i]]
print(c)

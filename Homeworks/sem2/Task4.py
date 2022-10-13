#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

import random

a = int(input('Input integer number: '))
spisok_random = []
for i in range (a):
    spisok_random.append(random.randint(-a,a))
print(spisok_random)
print(spisok_random[int(input(f'Input first position from 1 to {a}: '))-1]*spisok_random[int(input(f'Input second position from 1 to {a}: '))-1])
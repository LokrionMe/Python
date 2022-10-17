# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
str_sum = ''
sum = 0
spisok_random = []
for i in range(10):
    spisok_random.append(random.randint(-10, 10))
    if i % 2 != 0:
        str_sum += str(spisok_random[i]) + ' '
        sum += spisok_random[i]
print(f'In list {spisok_random} numbers on odd positions: {str_sum}, and sum = {sum}')
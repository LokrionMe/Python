# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
spisok_random = [random.randint(-10, 10) for i in range(10)]
print(
    f'In list {spisok_random} numbers on odd positions: {spisok_random[1::2]}, and sum = {sum(spisok_random[1::2])}')

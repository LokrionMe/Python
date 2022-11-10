# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
spisok_random = [
    random.randint(-10, 10) + random.randint(10, 100)/100
    for i in range(random.randint(3, 10))
]
for i in range(len(spisok_random)):
    if spisok_random[i] < 0:
        spisok_random[i] *= (-1)
        spisok_random[i] = spisok_random[i] % 1
        spisok_random[i] *= (-1)
    else:
        spisok_random[i] = spisok_random[i] % 1
print(f'{max(spisok_random)} - {min(spisok_random)} = {round(max(spisok_random) - min(spisok_random),2)}')

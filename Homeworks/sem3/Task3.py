# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#практически везде пришлось добавлять round,
#так как практически всегда выскакивают числа формата "3.2800000000000002"
import random
spisok_random = []
for i in range(random.randint(3, 10)):
    spisok_random.append(
        (random.randint(-10, 10) + random.randint(10, 100)/100))
for i in range(len(spisok_random)):
    if spisok_random[i] < 0:
        spisok_random[i] *= (-1)
        spisok_random[i] = round(spisok_random[i] % 1, 2)
        spisok_random[i] *= (-1)
    else:
        spisok_random[i] = round(spisok_random[i] % 1, 2)
max = spisok_random[0]
min = spisok_random[0]
for i in range(1, len(spisok_random)):
    if spisok_random[i] > max:
        max = spisok_random[i]
    if spisok_random[i] < min and spisok_random[i] != 0:
        min = spisok_random[i]
print(f'{max} - {min} = {round(max - min,2)}')

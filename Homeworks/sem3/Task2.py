# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
spisok_random = []
for i in range(random.randint(2, 10)):
    spisok_random.append(random.randint(-10, 10))
print(spisok_random)
spisok_mult = []
for i in range(len(spisok_random)//2+len(spisok_random)%2):
    spisok_mult.append(spisok_random[i]*spisok_random[0-1-i])
print(spisok_mult)
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
spisok_random = [random.randint(-10, 10) for i in range(random.randint(2, 10))]
print(spisok_random)
spisok_mult = [spisok_random[i]*spisok_random[-1-i]
               for i in range(len(spisok_random)//2+len(spisok_random) % 2)]
print(spisok_mult)

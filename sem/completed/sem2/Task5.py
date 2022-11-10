# Реализуйте алгоритм перемешивания списка.

import random

a = int(input('Input integer number: '))
spisok_random = [random.randint(-a, a) for i in range(a)]
print(spisok_random)
for i in range(int(len(spisok_random)/2)):
    pos1 = spisok_random[random.randint(0, a-1)]
    pos2 = spisok_random[random.randint(0, a-1)]
    temp = spisok_random[pos1]
    spisok_random[pos1] = spisok_random[pos2]
    spisok_random[pos2] = temp
print(spisok_random)

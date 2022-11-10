#  Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

import random


def lst_of_num(x):
    lst_x = []
    for i in range(2, x+1):
        while x % i == 0:
            lst_x.append(i)
            x = x//i
    return lst_x


a = lst_of_num(random.randint(2, 100))
b = lst_of_num(random.randint(2, 100))
print(a, b)
NOK = 1
for i in range(len(a)):
    NOK *= a[i]
i = 0
while i < len(b):
    while b[i] in a:
        a.remove(b[i])
        b.remove(b[i])
    NOK *= b[i]
    i += 1
print(NOK)

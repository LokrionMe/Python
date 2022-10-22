#  Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

import random
a = random.randint(2, 100)
b = random.randint(2, 100)
print(a, b)
lst_a = []
lst_b = []
for i in range(2, a+1):
    while a % i == 0:
        lst_a.append(i)
        a = a//i
print(lst_a)
for i in range(2, b+1):
    while b % i == 0:
        lst_b.append(i)
        b = b//i
print(lst_b)
NOK = 1
for i in range(len(lst_a)):
    NOK *= lst_a[i]
print(NOK)
i = 0
while i < len(lst_b):
    while lst_b[i] in lst_a:
        lst_a.remove(lst_b[i])
        lst_b.remove(lst_b[i])
    NOK *= lst_b[i]
    i += 1
print(NOK)
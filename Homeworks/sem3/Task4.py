# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import random
a = random.randint(2,100)
two_bit = ''
print (a)
while a!= 0:
    two_bit = str(a%2) + two_bit
    a = a//2
print (two_bit)
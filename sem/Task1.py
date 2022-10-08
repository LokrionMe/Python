#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#*Примеры:*
#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет

from this import d


a = int(input('Input first number: '))
b = int(input('Input second number: '))
if a**2 == b:
    print('yes')
else:
    print('no')

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

d = int(input('Input number: '))
for i in range(4):
    c = int(input('Input number: '))
    if c > d:
        d = c
print(f'Max = {d}')
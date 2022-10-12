#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

d = int(input('Input number: '))
for i in range(4):
    c = int(input('Input number: '))
    if c > d:
        d = c
print(f'Max = {d}')
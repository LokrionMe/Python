# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

a = list(input('Input number: '))
if a.count(',') != 0:
    a.remove(',')
if a.count('.') != 0:
    a.remove('.')
print(sum(map(int, a)))

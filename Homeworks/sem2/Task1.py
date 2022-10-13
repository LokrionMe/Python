# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11
sum = 0
a = list(input('Input number: '))
if a.count(',') != 0:
    a.remove(',')
if a.count('.') != 0:
    a.remove('.')
for i in range(len(a)):
    sum += int(a[i])
print(sum)

# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Input number: '))
if a > 7:
    a = a % 7
if a > 5:
    print('Weekend')
else:
    print('NOT weekend')

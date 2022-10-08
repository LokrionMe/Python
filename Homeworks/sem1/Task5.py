# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x1 = float(input('Input x1: '))
y1 = float(input('Input y1: '))
x2 = float(input('Input x2: '))
y2 = float(input('Input y2: '))
print(((x2-x1)**2+(y2-y1)**2)**0.5)
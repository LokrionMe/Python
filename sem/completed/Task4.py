#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90
def input_number():
    return input('Input number: ')
print(max(list(int(input_number()) for i in range (5))))
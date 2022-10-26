#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#*Примеры:*
#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет
def ch_kv(a, b):
    return a**2==b
def input_number():
    return input('Input number: ')
if ch_kv(int(input_number()),int(input_number())):
    print('Yes')
else:
    print('No')
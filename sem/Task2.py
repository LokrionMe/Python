def input_number():
    return input('Input number: ')

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

a = int(input_number())
for i in range(-a, a+1):
    print(i, end=', ')
print('\b\b\n')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

b = str(input_number())
for i in range(0, len(b)):
    if b[i] == ',':
        print(b[i+1])
        break
    if i == len(b)-1:
        print('no')

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

c = int(input_number())
if ((c%5==0 and c%10==0) or (c%15== 0)) and (c%30 !=0):
    print(True)
else: print(False)
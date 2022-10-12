def input_number():
    return input('Input number: ')

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

c = int(input_number())
if ((c%5==0 and c%10==0) or (c%15== 0)) and (c%30 !=0):
    print(True)
else: print(False)
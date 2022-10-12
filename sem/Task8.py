# Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

a = str(input('Input string: '))
b = str(input('Input key: '))
k = 0
for i in range(len(a)-1):
    if a[i:(i + len(b))] == b:
        k += 1
print(f'In string "{a}" key "{b}" is {k} times')
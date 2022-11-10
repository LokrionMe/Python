# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
a = abs(int(input('Input integer number: ')))
num_a = []
for i in range(2, a+1):
    k = 0
    for j in range(2, i+1):
        if i % j == 0:
            k += 1
        if j == i and k == 1:
            while a % i == 0:
                a = a // i
                num_a.append(i)
    if a == 1:
        break
print(num_a)

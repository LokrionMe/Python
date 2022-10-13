# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

fact = [1]
a = int(input('Input unteger number: '))
for i in range(1, a+1):
    fact.append(fact[i-1]*i)
fact.remove(1)
print(fact)

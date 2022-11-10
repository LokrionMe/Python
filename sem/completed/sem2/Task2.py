# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def mult(a):
    c = 1
    for i in range(1, a+1):
        c *= i
    return c


a = [i for i in range(1, int(input('Input unteger number: '))+1)]
print(list(map(mult, a)))

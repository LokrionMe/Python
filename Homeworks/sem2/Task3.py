# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} // это же вид словаря, но никак не списка, 
#                                                  а в задании нужно задать список
#     Сумма 9.06

# 1 вариант, если составлять словарь
n = int(input('Input integer number: '))
summa = 0.0
summa_chisel = {n:(1+1/n)**n for n in range(1,n+1)}
for i in range (1,len(summa_chisel)+1):
    summa += summa_chisel[i]
print(summa)

#2 вариант, если составлять список
n = int(input('Input integer number: '))
summa = 0.0
summa_chisel = []
for i in range (1, n+1):
    summa_chisel.append((1+1/i)**i)
for i in range(len(summa_chisel)):
    summa += summa_chisel[i]
print(summa)
# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
d = input('Input d: ')
if ' ' in d:
    d = d.replace(' ', '')
k = 1
pi = 3
for i in range(2, len(d)**4, 2):
    b = 1
    b *= i
    for j in range(1, 3):
        b *= (i+j)
    if k % 2 == 0:
        a = -4/b
    else:
        a = 4/b
    pi += a
    k += 1
print(str(pi)[:len(d)])

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def input_number():
    return input('Input number: ')


N = int(input_number())
d = {a: 3*a + 1 for a in range(1, N+1)}
print(d)

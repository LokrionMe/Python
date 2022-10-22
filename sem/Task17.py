# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# вводим из файла
def find_cof(urav:str)->list:
    st_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    urav = urav.replace(' ', '')
    urav = urav.replace('-', '+-')[:-2]
    urav = urav.replace('**', '^')
    for i in range(len(st_list)):
        urav = urav.replace(st_list[i], '^' + str(i))
    urav = urav.split('+')
    if urav[0] == '':
        urav = urav[1::]
    print(urav)
    for i in range(len(urav)):
        if urav[i][0:2] == '-x':
            urav[i] = urav[i].replace('-x','-1x')
        if urav[i][0] == 'x':
            urav[i] = urav[i].replace('x', '1x')
    len_st = int(urav[0].split('^')[1])
    urav.reverse()
    cof_st = []
    for i in range(len(urav)):
        for j in range(len_st + 1):
            if i == 0:
                if 'x' not in urav[i]:
                    cof_st.append(int(urav[i]))
                    break
                else:
                    cof_st.append(0)
            if i == 0 or i == 1:
                if 'x' == urav[i][-1]:
                    cof_st.append(int(urav[i].split('x')[0]))
                    break
                if len(cof_st) == 1:
                    cof_st.append(0)
            if '^' in urav[i]:
                if j == int(urav[i].split('^')[1]):
                    cof_st.append(int(urav[i].split('x')[0]))
                    break
                if j == len(cof_st):
                    cof_st.append(0)
    return cof_st
with open('Task17.txt', 'r', encoding="utf-8") as data:
        ur = data.readline()
print(ur)
cof_st = find_cof(ur)
print(cof_st)
a = cof_st[2]
b = cof_st[1]
c = cof_st[0]
disc = b**2 - 4 * a*c
print(disc)
if disc < 0:
    print('resheniy net')
if disc == 0:
    x = (-b) / (2*a)
    print(x)
if disc > 0:
    x1 = ((-b)+disc**(1/2))/(2*a)
    x2 = ((-b)-disc**(1/2))/(2*a)
    print(x1, x2)


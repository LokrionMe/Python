def find_cof(urav: str) -> list:
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
            urav[i] = urav[i].replace('-x', '-1x')
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


ind = {0: '\u2070',
       1: '\u00B9',
       2: '\u00B2',
       3: '\u00B3',
       4: '\u2074',
       5: '\u2075',
       6: '\u2076',
       7: '\u2077',
       8: '\u2078',
       9: '\u2079'}

with open('1st ex.txt', 'r', encoding='utf-8') as data:
    lst_first = data.readline()
with open('2nd ex.txt', 'r', encoding='utf-8') as data:
    lst_second = data.readline()
lst_first = find_cof(lst_first)
lst_second = find_cof(lst_second)
while len(lst_first) != len(lst_second):
    if len(lst_first) < len(lst_second):
        lst_first.append(0)
    else:
        lst_second.append(0)
lst_third = []
for i in range(len(lst_first)):
    lst_third.append(lst_first[i]+lst_second[i])
sum_cof = ' = 0'
for i in range(len(lst_third)):
    if lst_third[i] != 0:
        if lst_third[i] > 1:
            lst_third[i] = '+' + str(lst_third[i])
        if i == 0:
            if lst_third[i] == 1:
                lst_third[i] = '+1'
            sum_cof = ' ' + str(lst_third[i]) + sum_cof
        if lst_third[i] == -1:
            lst_third[i] = '-'
        if lst_third[i] == 1:
            lst_third[i] = '+'
        if i == 1:
            sum_cof = ' ' + str(lst_third[i]) + 'x' + sum_cof
        if 1 < i < 10:
            sum_cof = ' ' + str(lst_third[i]) + 'x' + ind[i] + sum_cof
        if i >= 10:
            sum_cof = ' ' + str(lst_third[i]) + 'x' + \
                ind[i//10] + ind[i % 10] + sum_cof
if sum_cof[1] == '+':
    sum_cof = sum_cof[2::]
else:
    sum_cof = sum_cof[1::]
with open('sum.txt', 'w', encoding = 'utf-8') as data:
    data.write(sum_cof)
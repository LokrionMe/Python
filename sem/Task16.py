#  Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.

a = ''
with open ('file.txt', 'r') as data:
    for i in data:
        a = a + i
a = a.split(' ')
print (a)
min_num = int(a[0])
max_num = int(a[0])
for i in range (len(a)):
    if int(a[i]) > max_num:
        max_num = int(a[i])
    if int(a[i]) < min_num:
        min_num = int(a[i])
print (min_num, max_num)
# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []
a= input('Input numbers: ')
check_num = [0,1,2,3,4,5,6,7,8,9]
b=[]
for i in range(len(check_num)):
  k=0
  for j in range(len(a)):
    if str(check_num[i]) == a[j]:
      k+=1
  if k == 1:
    b.append(check_num[i])
print (b)
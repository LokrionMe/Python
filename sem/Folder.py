import os
import random

def check_names():
    way = 'D:'
    files_list = os.listdir(way)
    return files_list

def del_num(files_list):
    for i in range(1,len(files_list)):
        if files_list[i] != 'RAMMST~1.MP4':
            a = files_list[i].find(' ')
            os.rename(f'D:\{files_list[i]}',f'D:\{files_list[i][a::]}')

def add_num(files_list):
    for i in range(1,len(files_list)):
        if files_list[i] != 'RAMMST~1.MP4':
            os.rename(f'D:\{files_list[i]}',f'D:\{random.randint(1,999)}{files_list[i]}')
files_list = check_names()
del_num(files_list)
files_list = check_names()
add_num(files_list)

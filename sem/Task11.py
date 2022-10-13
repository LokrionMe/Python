# Create a function taking a positive integer as its parameter and returning a string
# containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the
# left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered:
# 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII;
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'
# Help:
# Symbol Value
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1,000

# Remember that there can't be more than 3 identical symbols in a row.
# b=0
# c=0
# d=0
# e=0
# f=0
# g=0
# h=0
# a = 1996
# while a != 0:
#     if a // 1000 > 0:
#         b = a//1000
#         a = a % 1000
#     if a // 500 > 0:
#         c = a//500
#         a = a % 500
#     if a // 100 > 0:
#         d = a//100
#         a = a % 100
#     if a // 50 > 0:
#         e = a//50
#         a = a % 50
#     if a // 10 > 0:
#         f = a//10
#         a = a % 10
#     if a // 5 > 0:
#         g = a//5
#         a = a % 5
#     if a // 1 > 0:
#         h = a//1
#         a = a % 1
# print(f'M = {b}, D = {c}, C = {d}, L = {e}, X = {f}, V = {g}, I = {h}')


# a = str(1998)
# if len(a)==4:
    
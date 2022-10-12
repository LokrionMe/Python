# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81



# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

#
# Write a function that takes an integer as input, and returns the number of bits
# that are equal to one in the binary representation of that number. You can guarantee that input is no
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

# ----------------------------------

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3]) == [1,2,3]

# ----------------------------------

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
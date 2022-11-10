# Write a function that takes an integer as input, and returns the number of bits
# that are equal to one in the binary representation of that number. You can guarantee that input is no
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def input_number():
    return input('Input number: ')
a = str(bin(int(input_number())))[2::]
print(sum([1 for i in range(len(a)) if a[i] == '1']))
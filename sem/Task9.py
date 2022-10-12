# Write a function that takes an integer as input, and returns the number of bits
# that are equal to one in the binary representation of that number. You can guarantee that input is no
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

a = str(bin(int(input('Input integer number: '))))
a = a[2:]
k = 0
for i in range (len(a)):
    if a[i] == '1':
        k += 1
print(k)
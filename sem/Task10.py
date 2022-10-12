# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.
# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3]) == [1,2,3]

a = str(input('Input string of letters or numbers: '))
i = 0
while i < len(a)-1:
    while a[i] == a[i+1]:
        a = a[0:i]+a[i+1:]
        if i == len(a)-1:
            break
    i += 1
print(list(a))

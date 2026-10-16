# Write a Python program to count the frequency of characters in a string using a dictionary.
# Input aabcc
# Expected Output {'a': 2, 'b': 1, 'c': 2}

s1 = 'aabcc'

d1 = {}

for x in s1:
    if x in d1:
        d1[x] += 1
    else:
        d1[x] = 1

print(d1)
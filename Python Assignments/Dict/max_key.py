# 13. Write a Python program to find the key with the maximum value in a dictionary.
# Input {"A": 75, "B": 92, "C": 88}
# Expected Output Key with maximum value = B

d1 = {"A": 75, "B": 92, "C": 88}

maximum = 0
max_key = " "

for i , j in d1.items():
    if j > maximum:
        maximum = j
        max_key = i


print('Max = ', max_key)
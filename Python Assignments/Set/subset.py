# 7. Write a Python program to check whether one set is a subset of another set.
# Input A = {1, 2}
# B = {1, 2, 3, 4}
# Expected Output A is a subset of B = True


A = {1, 2}
B = {1, 2, 3, 4}

C = A.issubset(B)

print('A is a subset of B =', C)
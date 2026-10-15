# Write a Python program to find the union of two sets.
# Input A = {1, 2, 3}
# B = {3, 4, 5}
# Expected Output {1, 2, 3, 4, 5}


A = {1, 2, 3}
B = {3, 4, 5}

C = A.union(B)
print(C)

#-----------------------------------------
#sol-2

A = {1, 2, 3}
B = {3, 4, 5}

C = A | B
print(C)
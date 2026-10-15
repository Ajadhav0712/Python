# 4. Write a Python program to find the intersection of two sets.
# Input A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Expected Output {3, 4}


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.intersection(B)

print(C)

#-------------------------------------------------
#sol -2

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A & B

print(C)

#-------------------------------------------------
#sol -3

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)



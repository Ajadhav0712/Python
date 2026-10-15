# 6. Write a Python program to find the symmetric difference between two sets.
# Input A = {1, 2, 3}
# B = {3, 4, 5}
# Expected Output {1, 2, 4, 5}

A = {1, 2, 3}
B = {3, 4, 5}

C = A.symmetric_difference(B)

print(C)

#----------------------------
# Sol - 2

A = {1, 2, 3}
B = {3, 4, 5}

C = A ^ B
print(C)

#----------------------------
# Sol - 3

A = {1, 2, 3}
B = {3, 4, 5}

A.symmetric_difference_update(B)
print(A)
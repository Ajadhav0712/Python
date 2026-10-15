# 5. Write a Python program to find the difference between two sets.
# Input A = {1, 2, 3, 4}
# B = {3, 4, 5}
# Expected Output A - B = {1, 2}

A = {1, 2, 3, 4}
B = {3, 4, 5}

C = A.difference(B)

print(C)

#------------------------------------------
#Sol -2
A = {1, 2, 3, 4}
B = {3, 4, 5}

C = A - B

print(C)

#------------------------------
#Sol3
A = {1, 2, 3, 4}
B = {3, 4, 5}

A.difference_update(B)
print(A)
# 14. Write a Python program to update a set with elements from another iterable.
# Input Set = {1, 2}
# Iterable = [3, 4, 5]
# Expected Output {1, 2, 3, 4, 5}

s1 = {1, 2}
l1 = [3, 4, 5]

s1.update(l1)

print(s1)
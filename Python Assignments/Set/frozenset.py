# 15. Write a Python program to create a frozen set and demonstrate its usage.
# Input [1, 2, 3, 4]
# Expected Output frozenset({1, 2, 3, 4})
# Modification is not allowed.

l1 = [1, 2, 3, 4]

fs = frozenset(l1)

print(fs)

try:
    fs.add(5)

except:

    print('modification not allowed')
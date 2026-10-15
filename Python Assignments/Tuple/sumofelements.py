# 16. Write a Python program to find the sum of numeric elements in a tuple.
# Input (10, 20, 30, 40)
# Expected Output Sum = 100

t1 = (10, 20, 30, 40)

total = 0
for x in t1:
    total += x

print(total)


########--------------------
# sol -2

total = sum(t1)
print(total)
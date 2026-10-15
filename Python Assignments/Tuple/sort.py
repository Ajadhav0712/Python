# 12. Write a Python program to sort tuple elements and display the result.
# Input (5, 2, 8, 1, 4)
# Expected Output (1, 2, 4, 5, 8)

t1 = (5, 2, 8, 1, 4)

t2 = tuple(sorted(t1))
print(t2)
#-----------------------

# sol-2

t1 = (5, 2, 8, 1, 4)

l1 = list(t1)
l1.sort(reverse=True)
t2 = tuple(l1)
print(t2)


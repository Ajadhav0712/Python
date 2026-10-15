# 14. Write a Python program to create a nested tuple and access its inner elements.
# Input (1, 2, (10, 20, 30))
# Expected Output Inner tuple = (10, 20, 30)
# Second inner element = 20


t1 = (1, 2, (10, 20, 30))

inner = t1[2]

print('Inner tuple', inner)
print('Second inner element', inner[1])
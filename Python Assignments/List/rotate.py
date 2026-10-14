# Write a Python program to rotate a list by n positions.
# Input List = [1, 2, 3, 4, 5]
# n = 2
# Expected Output Rotated list = [3, 4, 5, 1, 2]

l1 = [1, 2, 3, 4, 5]
n = 2

for i in range (n):
    first = l1.pop(0)
    l1.append(first)

print('Rotation list =', l1)
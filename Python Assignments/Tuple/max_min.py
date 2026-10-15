# 6. Write a Python program to find the maximum and minimum values in a tuple.
# Input (8, 3, 15, 1, 9)
# Expected Output Maximum = 15, Minimum = 1


t1 = (8, 3, 15, 1, 9)

maximum = t1[0]
minimum = t1[0]

for x in t1:
    if x > maximum:
        maximum =x
    if x < minimum:
        minimum = x

print('Max =', maximum)
print('Min =', minimum)

#--------------------------------
#Sol-2

print('Max =', max(t1))
print('Min =', min(t1))
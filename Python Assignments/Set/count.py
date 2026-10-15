# 12. Write a Python program to count the number of elements in a set.
# Input {10, 20, 30, 40, 50}
# Expected Output Number of elements = 5


s1 = {10, 20, 30, 40, 50}

print('Number of elements =', len(s1))

#--------------------------------
#sol -2

count = 0

for x in s1:
    count +=1

print('Number of elements =', count)
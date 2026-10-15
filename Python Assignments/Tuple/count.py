# Write a Python program to count the occurrences of an element in a tuple.
# Input Tuple = (1, 2, 2, 3, 2, 4)
# Element = 2
# Expected Output Occurrences of 2 = 3


T1 = (1, 2, 2, 3, 2, 4)
ele = 2

count = 0

for x in T1:
    if x==ele:
        count += 1

print('Occurrences of 2 =', count)

#-----------------------------------------

count1 = T1.count(ele)
print('Occurrences of 2 =', count1)
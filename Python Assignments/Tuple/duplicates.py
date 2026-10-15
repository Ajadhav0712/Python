# 13. Write a Python program to remove duplicate values from a tuple.
# Input (1, 2, 2, 3, 1, 4)
# # Expected Output (1, 2, 3, 4)

t1 = (1, 2, 2, 3, 1, 4)

s1 = set(t1)
t2 = tuple(s1)
print(t2)


#--------------------------------
#sol -2
t2 = ()

for x in t1:
    if x in t1 and x not in t2:
        t2 += (x,)

print(t2)
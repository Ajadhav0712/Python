# Write a Python program to concatenate two tuples.
# Input Tuple 1 = (1, 2, 3)
# Tuple 2 = (4, 5)
# Expected Output (1, 2, 3, 4, 5)

T1 = (1, 2, 3)
T2 = (4, 5)

T3 = T1 + T2

print(T3)


#--------------------------------------
#sol-2

t1 = (1, 2, 3)
t2 = (4, 5)


t3 = (*t1, *t2)
print(t3)

#----------------------------
#sol -3

temp = list(t1)
temp.extend(t2)
t3 = tuple(temp)

print(t3)


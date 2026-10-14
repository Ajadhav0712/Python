# 14. Write a Python program to find common elements between two lists.
# Input List 1 = [1, 2, 3, 4]
# List 2 = [3, 4, 5, 6]
# Expected Output Common elements = [3, 4]


l1 = [1, 2, 3, 3, 4]
l2 = [3, 4, 5, 6]

com = []

for x in l1:
    for i in l2:
        if x == i and x not in com:
            com.append(x)

print(com)

#---------------------------------------------
#approach -2

com1 = [x for x in l1 if x in l2 ]
com1 = list(set(com1))
print(com1)




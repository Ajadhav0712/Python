# 15. Write a Python program to create a new list containing squares of all elements of a list.
# Input [1, 2, 3, 4, 5]
# Expected Output [1, 4, 9, 16, 25]



l1 = [1, 2, 3, 4, 5]

l2 = []
for x in l1:
    x *=x
    l2.append(x)

print(l2)

#-----------------------------------------
#Approach -2

sq_list = [x * x for x in l1]
print(sq_list)

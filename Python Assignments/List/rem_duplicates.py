# 5. Write a Python program to remove duplicate elements from a list.
# Input [1, 2, 2, 3, 1, 4]
# Expected Output [1, 2, 3, 4]

my_list = [1, 2, 2, 3, 1, 4]

new_list = []

for x in my_list:
    if x not in new_list:
        new_list.append(x)

print('without duplicates list is', new_list)


#-------------------------------------
#Approach 2

my_list1 = [1, 2, 2, 3, 1, 4]

unique_list = list(set(my_list))

print('unique_list=', unique_list)
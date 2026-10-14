# 7. Write a Python program to merge two lists into a single list.
# Input List 1 = [1, 2, 3]
# List 2 = [4, 5, 6]
# Expected Output [1, 2, 3, 4, 5, 6]


list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)



#-----------------------------------
#Approch-2
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

merge_list = my_list1+my_list2

print(merge_list)


#-----------------------------------
#approch 3
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

for x in my_list2:
    my_list1.append(x)

print(my_list1)
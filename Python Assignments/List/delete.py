# Write a Python program to delete all occurrences of a given element from a list.
# Input List = [1, 2, 3, 2, 4, 2]
# Delete = 2
# Expected Output [1, 3, 4]


my_list = [1, 2, 3, 2, 4, 2]
delete = 2
new_list = []

for x in my_list:
    if x != delete:
        new_list.append(x)

print(new_list)



#--------------------------------
#Approch-2

new_list1 = [x for x in my_list if x != delete]
print(new_list1)

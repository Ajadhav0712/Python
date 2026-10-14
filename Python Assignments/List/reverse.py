# 6. Write a Python program to reverse a list without using the reverse() method.
# Input [10, 20, 30, 40]
# Expected Output [40, 30, 20, 10]


my_list = [10, 20, 30, 40]

rev_List = my_list[::-1]

print(rev_List)

#--------------------------------------
#Approch-2

my_list1 = [10, 20, 30, 40]

rev_List1 =[]

for x in range(len(my_list1)-1, -1, -1):
    rev_List1.append(my_list1[x])

print(rev_List1)

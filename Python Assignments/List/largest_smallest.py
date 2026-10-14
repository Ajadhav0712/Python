# Write a Python program to find the largest and smallest element in a list.
# Input [8, 3, 15, 1, 9]
# Expected Output Largest = 15, Smallest = 1


my_list = [8, 3, 15, 1, 9]

large = my_list[0]
small = my_list[0]

for x in my_list:
    if x > large:
        large = x
    if x < small:
        small = x
       
print('largest =', large)
print('smallest =', small)



#------------------------------------------------------------
#Alternative approch

print('largest =', max(my_list))
print('smallest =', min(my_list))
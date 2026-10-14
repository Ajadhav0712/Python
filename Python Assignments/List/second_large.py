# Write a Python program to find the second largest number in a list.
# Input [10, 40, 20, 30, 50]
# Expected Output Second largest = 40

my_list = [10, 40, 20, 30, 50]

my_list.sort()

print('second largest num =', my_list[-2])


#--------------------------------------------
#Approch -2
my_list1 = [10, 40, 20, 30, 50]

largest = float('-inf')
second_largest = float('-inf')

for x in my_list1:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x < largest:
        second_largest = x

print('Second_largest =', second_largest)

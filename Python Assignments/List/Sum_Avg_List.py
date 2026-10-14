# Write a Python program to find the sum and average of list elements.
# Input [10, 20, 30, 40]
# Expected Output Sum = 100, Average = 25.0

my_list = [10, 20, 30, 40]
# Calculate the sum of the list elements
total_sum = sum(my_list )
# Calculate the average of the list elements
average = total_sum / len(my_list) 

print('sum = ', total_sum)
print('Average = ', average)


#----------------------------------------------
#'Alternative solution'

my_list1 = [10, 20, 30, 40]

sum = 0

for x in my_list1:
    sum += x

print('sum', sum)

print('Avg =', sum/len(my_list1))

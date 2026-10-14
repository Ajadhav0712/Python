# 9. Write a Python program to sort a list in ascending and descending order.
# Input [5, 2, 8, 1, 4]
# Expected Output Ascending = [1, 2, 4, 5, 8]
# Descending = [8, 5, 4, 2, 1]

samplelist = [5, 2, 8, 1, 4]

asce_sort = sorted(samplelist)
desc_sort = sorted(samplelist, reverse=True)

print('Ascending sort =', asce_sort)
print(' Descending sort =', desc_sort)

#-----------------------------------------------------
#Approch: 2

samplelist1 = [5, 2, 8, 1, 4]


samplelist1.sort()
print("Ascending =", samplelist1)

samplelist1.sort(reverse=True)
print("Descending =", samplelist1)
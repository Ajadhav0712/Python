# 4. Write a Python program to count even and odd numbers in a list.
# Input [1, 2, 3, 4, 5, 6]
# Expected Output Even count =3 odd Count = 3


list1 = [1, 2, 3, 4, 5, 6]

even_count = 0
odd_count = 0

for x in list1:
    if x%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print('Even Count=', even_count)
print('Odd Count=', odd_count)

#---------------------------------------------
#alternative approach

list2 = [1, 2, 3, 4, 5, 6]

even = [x for x in list2 if x%2 ==0]
odd = [x for x in list2 if x%2 !=0]

print('Even Count=',len(even))
print('Odd Count=', len(odd))
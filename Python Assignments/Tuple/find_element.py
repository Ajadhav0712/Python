# Write a Python program to check whether an element exists in a tuple.
# Input Tuple = (10, 20, 30)
# Element = 20
# Expected Output 20 exists in the tuple.


t1 = (10, 20, 30)
ele = 20


if ele in t1:
    print(f'{ele} exists in the tuple')


#--------------------------------------
#sol -2

for x in t1:
    if x == ele:
        print(f'{ele} exists in the tuple')
        break


# 4. Write a Python program to find the index of an element in a tuple.
# Input Tuple = (10, 20, 30, 40)
# Element = 30
# Expected Output Index = 2


sample_tuple = (10, 20, 30, 40, 30)
ele = 30

print(f'Index of {ele}={sample_tuple.index(30)}')


#--------------------------------------------------
#Solution -2

if ele in sample_tuple:
    print(f'Index of {ele}={sample_tuple.index(ele)}')

else:
    print(f'{ele} not found')


#-------------------------------------
#sol -3

for i, x in enumerate(sample_tuple):
    if x == ele:
        print(f"{ele} found at index {i}")



#-------------------------------------
#sol -4

indexes = [i for i, x in enumerate(sample_tuple) if x == ele]
print(f"Indexes = {indexes}")  
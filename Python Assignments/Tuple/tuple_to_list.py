# 5. Write a Python program to convert a tuple into a list and a list into a tuple.
# Input Tuple = (1, 2, 3)
# List = [4, 5, 6]
# Expected Output Tuple to List = [1, 2, 3]
# List to Tuple = (4, 5, 6)

t1 = (1, 2, 3)
l1 = [4, 5, 6]

TupletoList = list(t1) 
ListtoTuple = tuple(l1)

print('Tuple to List =', TupletoList)
print('List to Tuple =', ListtoTuple)
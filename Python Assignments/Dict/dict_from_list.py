# 10. Write a Python program to create a dictionary from two lists: one of keys and one of values.
# Input Keys = ['name', 'age', 'city']
# Values = ['Amit', 21, 'Kolhapur']
# Expected Output {'name': 'Amit', 'age': 21, 'city': 'Kolhapur'}


key = ['name', 'age', 'city']
val = ['Amit', 21, 'Kolhapur']


d1 = {}

for i in range(len(key)):
    d1[key[i]] = val[i]


print(d1)


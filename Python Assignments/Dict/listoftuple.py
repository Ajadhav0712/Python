# 14. Write a Python program to convert a dictionary into a list of tuples.
# Input {"a": 1, "b": 2, "c": 3}
# Expected Output [('a', 1), ('b', 2), ('c', 3)]

d1 = {"a": 1, "b": 2, "c": 3}

l1 = list(d1.items())

print(l1)


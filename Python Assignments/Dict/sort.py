# 11. Write a Python program to sort a dictionary by keys.
# Input {"c": 3, "a": 1, "b": 2}
# Expected Output {'a': 1, 'b': 2, 'c': 3}

d1 = {"c": 3, "a": 1, "b": 2}
d2 = {}
d2 = sorted(d1.items())

print(d2)

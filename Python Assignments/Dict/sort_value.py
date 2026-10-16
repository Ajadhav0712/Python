# 12. Write a Python program to sort a dictionary by values.
# Input {"a": 30, "b": 10, "c": 20}
# Expected Output {'b': 10, 'c': 20, 'a': 30}

d1 = {"a": 30, "b": 10, "c": 20}

values = sorted(d1.values())

d2 = {}

for i in values:
    for k in d1:
        if d1[k] == i:
            d2[k] = i

print(d2)
    
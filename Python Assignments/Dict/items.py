# 6. Write a Python program to print all keys, all values, and all items of a dictionary.
# Input {"a": 10, "b": 20}
# Expected Output Keys = ['a', 'b']
# Values = [10, 20]
# Items = [('a', 10), ('b', 20)]

d1 = {"a": 10, "b": 20}

k = list(d1.keys())
v = list(d1.values())
i = list(d1.items())

print('Keys =', k )
print('Values =', v)
print('Items = ', i)
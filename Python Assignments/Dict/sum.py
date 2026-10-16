# 7. Write a Python program to find the sum of all numeric values in a dictionary.
# Input {"a": 10, "b": 20, "c": 30}
# Expected Output Sum = 60


d1 = {"a": 10, "b": 20, "c": 30}

Total = 0

for values in d1.values():
    Total += values

print('sum =', Total)


#-------------------------------
# sol -2

print('sum =', sum(d1.values()))
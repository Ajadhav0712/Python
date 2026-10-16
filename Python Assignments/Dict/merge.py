# 8. Write a Python program to merge two dictionaries.
# Input D1 = {"a": 1, "b": 2}
# D2 = {"c": 3, "d": 4}
# Expected Output {"a": 1, "b": 2, "c": 3, "d": 4}

D1 = {"a": 1, "b": 2}
D2 = {"c": 3, "d": 4}


D1.update(D2)

print(D1)

#---------------------------
# Sol -2

D3 = D1 | D2 

print(D3)
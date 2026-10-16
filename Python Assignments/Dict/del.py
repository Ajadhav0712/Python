# 4. Write a Python program to delete a key from a dictionary.
# Input Dictionary = {"a": 1, "b": 2, "c": 3}
# Delete key = b
# Expected Output {"a": 1, "c": 3}


d1 = {"a": 1, "b": 2, "c": 3}

d1.pop("c")

print(d1)

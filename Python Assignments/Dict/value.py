# 3. Write a Python program to update the value of an existing key in a dictionary.
# Input Dictionary = {"name": "Amit", "age": 20}
# Update age = 21
# Expected Output {"name": "Amit", "age": 21}

dict1 = {"name": "Amit", "age": 20}

dict1["age"] = 21

print(dict1)


#---------------------------------------
#sol -2

dict2 = {"name": "Amit", "age": 20}
dict2.update({"age": 21})
print(dict2)
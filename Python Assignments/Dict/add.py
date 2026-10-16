# 2. Write a Python program to add a new key-value pair to a dictionary.
# Input Dictionary = {"name": "Amit"}
# Add: "city": "Kolhapur"
# Expected Output {"name": "Amit", "city": "Kolhapur"}

dict1 = {"name": "Amit"}

dict1["city"] = "Kolhapur"

print(dict1)


#--------------------------------------
#Sol -2
dict2 = {"name": "Amit"}

dict2.update({"city": "Kolhapur"})

print(dict2)
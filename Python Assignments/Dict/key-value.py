# Write a Python program to create a dictionary and display all key-value pairs.
# Input {"name": "Amit", "age": 21}
# Expected Output name: Amit
# age: 21


Dict1= {"name": "Amit", "age": 21}
Dict1.items()

print("The key-value pairs in the dictionary are:", Dict1.items())


#-----------------------------------------------
#sol-2

for key, value in Dict1.items():
    print(key, ":", value)
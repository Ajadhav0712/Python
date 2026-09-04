# Write a Python program to count uppercase letters, lowercase letters, digits, and special characters in a
# string.
# Input LihaTech@2026
# Expected Output Uppercase = 2, Lowercase = 6, Digits = 4, Special = 1


str1 = input("Enter the string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for char in str1:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase = ", uppercase)
print("Lowercase = ", lowercase)
print("Digits = ", digits)
print("Special = ", special)

# Alternative solution with sum 

str2 = input("Enter the string: ")
uppercase2 = sum(1 for char in str2 if char.isupper())  
lowercase2 = sum(1 for char in str2 if char.islower())
digits2 = sum(1 for char in str2 if char.isdigit())
special2 = sum(1 for char in str2 if not char.isalnum())

print("Uppercase = ", uppercase2)
print("Lowercase = ", lowercase2)
print("Digits = ", digits2)
print("Special = ", special2)
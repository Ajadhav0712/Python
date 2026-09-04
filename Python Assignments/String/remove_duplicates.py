# 15. Write a Python program to remove duplicate characters from a string while preserving order.
# Input programming
# Expected Output Unique characters = progamin


str1 = input("Enter the string: ")
unique_chars = []

for char in str1:
    if char not in unique_chars:
        unique_chars.append(char)

print("Unique characters = ", "".join(unique_chars))

#Alternative solution
str2 = input("Enter the string: ")

unique_chars2 = ""
for char in str2:
    if char not in unique_chars2:
        unique_chars2 += char

print("Unique characters = ", unique_chars2)    
# Write a Python program to extract digits from a string.
# Input abc123xyz45
# Expected Output Digits = 12345


str1 = input("Enter the string: ")

digit = []

for i in str1:
    if i.isdigit():
        digit.append(i)

print("Digits :", "".join(digit))



# Alternative solution
str2 = input("Enter the string: ")
digit2 = [i for i in str2 if i.isdigit()]
print("Digits: ", "".join(digit2))
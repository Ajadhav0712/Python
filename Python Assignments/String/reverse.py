# Write a Python program to reverse a given string.
# Input Python
# Expected Output Reversed string = nohtyP


str1 = input("Enter the string: ")

rev_str = str1[: : -1]

print(rev_str)



# alternative sloution
k = input("Enter the string: ")
reversed_str = ''.join(reversed(k))
print(reversed_str)
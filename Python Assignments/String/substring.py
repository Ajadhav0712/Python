# Write a Python program to check whether a string starts and ends with a given substring.
# Input String: Python Programming
# Start: Python
# End: Programming
# Expected Output Starts with Python = True
# Ends with Programming = True


str1 = input("Enter the string: ")
start = input("Enter the starting substring: ") 
end = input("Enter the ending substring: ")

print("starts with python : ", str1.startswith(start))
print("ends with programming : ", str1.endswith(end))



# Alternative solution
str1 = input("Enter the string: ") 
start = input("Enter the starting substring: ")
end = input("Enter the ending substring: ")

if str1.startswith(start) and str1.endswith(end):
    print(" both conditions are True")
else:
    print(" one or both conditions are False")
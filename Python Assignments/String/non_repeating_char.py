# Write a Python program to find the first non-repeating character in a string.
# Input aabbcddee
# Expected Output First non-repeating character = c


string = input("Enter the string: ")
for char in string:
    if string.count(char) == 1:
        print("First non-repeating character: ", char)
    else:
        print
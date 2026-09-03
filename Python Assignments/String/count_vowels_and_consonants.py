# Write a Python program to count vowels and consonants in a string

# Input: Programming
# Expected Output Vowels = 3, Consonants = 8

str_input = input('Enter the String:')
str_input = str_input.replace(" ", "").lower()  # Remove spaces and convert to lowercase
Vowels = 0
Consonants = 0

for char in str_input:
    if char in 'aeiou':
        Vowels += 1
    else:
        Consonants += 1
print('Vowels =', Vowels, 'Consonants =', Consonants)

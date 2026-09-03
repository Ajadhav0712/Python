'''
A palindrome string is a word or phrase that reads the exact same backward as forward.
Examples: "racecar", "radar", and "level".
'''

#Write a Python program to check whether a string is a palindrome or not.
#Input: madam
#Expected Output: The string is a palindrome.

#k = 'madam'
k = input('Enter a String you want to check for palindrome:')

if k == k[::-1]:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')

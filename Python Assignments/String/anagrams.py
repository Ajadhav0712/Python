# Write a Python program to check whether two strings are anagrams
# input : listen and silent
# output : The strings are anagrams.

str1 = input('enter the first string:')
str2 = input('enter the second string:')

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()


if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
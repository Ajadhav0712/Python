# 16. Write a Python program to count the frequency of words in a sentence using a dictionary.
# Input python is easy and python is powerful
# Expected Output {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}


str1 = " python is easy and python is powerful"

words = str1.split()

d1 = {}

for word in words:
    if word in d1:
        d1[word] += 1
    else:
        d1[word] =1

print(d1)
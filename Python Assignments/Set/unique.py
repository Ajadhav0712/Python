# 16. Write a Python program to find common unique words from two sentences using sets.
# Input Sentence 1: python is easy and powerful
# Sentence 2: python is popular and useful
# Expected Output Common words = {'python', 'is', 'and'} (order may vary)


s1 = 'python is easy and powerful'
s2 = 'python is popular and useful'

set1 = set(s1.split())
set2 = set(s2.split())

common_words = set1.intersection(set2) 

print('Common words =', common_words)
# 13. Write a Python program to split a sentence into words and join them using a hyphen.
# Input Python is fun
# Expected Output Python-is-fun


sentence = input("Enter the sentence: ")
words = sentence.split()
result = "-".join(words)
print(result)


# Altrnative solution
sentence2 = input("Enter the sentence: ")
result2 = sentence2.replace(" ", "-")
print(result2)

#Alternative solution with loop
sentence3 = input("Enter the sentence: ")

words3 = sentence3.split()
result3 = ""
for word in words3:
    result3 += word + "-"
print(result3)
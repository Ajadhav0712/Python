# Write a Python program to replace a word in a string with another word.
# Input Sentence: I like Java
# Replace: Java with Python
# Expected Output I like Python

str1 = input("Enter a string: ")

result = str1.replace("Java", "Python")

print(result)



# Alternative solution

str2 = input("Enter a String")

word = str2.split()
new_word =[]
for w in word:
     if w == "Java":
        new_word.append("python")
     else:
        new_word.append(w)
result1 = " ".join(new_word)
print (result1)


# Alternative approch
k = input("enter the string")
old_word = input("world to replace: ")
new_word = input("Replace with: ")

r = k.replace(old_word, new_word)
print(r)
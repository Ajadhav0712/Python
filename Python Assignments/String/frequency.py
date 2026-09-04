# Write a Python program to find the frequency of each character in a string.
# Input aabcc
# Expected Output a: 2, b: 1, c: 2

# f = input("Enter the string:")

# count ={}
# for ch in f:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch] = 1
# for ch, fre in count.items():
#     print(f"{ch}: {fre}", end=" ")



 # Alternative solution

f1 = input("Enter the string: ")

count = {}
for ch in f1:
    count[ch] = count.get(ch, 0) + 1

result = ", ".join(f"{ch}: {fre}" for ch, fre in count.items())
print(result)   
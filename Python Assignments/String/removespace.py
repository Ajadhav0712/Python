# Write a Python program to remove all spaces from a string.
# Input Liha Tech Kolhapur
# Expected Output LihaTechKolhapur



k = input("Enter the string:")
r = k.replace(" ", "")
print (r)


# alternative solution
k1 = input("Enter the string:")
result = " ".join(k1.split())
print(result)

# alternative solution
k3 = input("Enter the string:")
result1 = "".join(ch for ch in k3 if ch != " ")
print (result1)
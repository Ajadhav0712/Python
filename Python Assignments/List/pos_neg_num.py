# Write a Python program to separate positive and negative numbers from a list.
# Input [-5, 3, -2, 7, 0, -1]
# Expected Output Positive = [3, 7]
# Negative = [-5, -2, -1]

l1 = [-5, 3, -2, 7, 0, -1]

positive = [i for i in l1 if i>=0]
negative = [i for i in l1 if i<0]

print('positive =', positive)
print('Negative =', negative)

#----------------------------------
#Approch -2

pos = []
neg = []

for x in l1:
    if x >= 0:
        pos.append(x)
    elif x < 0:
        neg.append(x)

print('positive =', pos)
print('Negative =', neg)

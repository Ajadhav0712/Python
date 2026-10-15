# 11. Write a Python program to unpack a tuple into separate variables.
# Input (101, "Amit", 85.5)
# Expected Output Roll = 101
# Name = Amit
# Marks = 85.5

t1 = (101, "Amit", 85.5)

(Roll, Name, Marks) = t1

print('Roll =', Roll)
print('Name =', Name)
print('Marks =', Marks)
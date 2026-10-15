# 15. Write a Python program to swap two tuples.
# Input Tuple A = (1, 2)
# Tuple B = (3, 4)
# Expected Output Tuple A = (3, 4)
# Tuple B = (1, 2)

tupleA = (1, 2)
tupleB = (3, 4)

temnp = tupleA
tupleA = tupleB
tupleB = temnp

print('tuple A =', tupleA)
print('tuple B', tupleB)
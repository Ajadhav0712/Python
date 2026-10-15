# 10. Write a Python program to create a tuple with repeated elements.
# Input Element = 5
# Repeat = 4
# Expected Output (5, 5, 5, 5)


ele = 5
repeat = 4  

t1 = (ele,) * repeat

print(t1)

#-----------------------------------

t1 =()
for i in range(repeat):
    t1 += (ele,)

print(t1)
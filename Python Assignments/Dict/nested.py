# 15. Write a Python program to create a nested dictionary for student details.
# Input Student 101: Name = Amit, Marks = 85
# Student 102: Name = Neha, Marks = 90
# Expected Output {101: {'name': 'Amit', 'marks': 85}, 102: {'name': 'Neha', 'marks': 90}}

Students = {
    101: {"name": "Amit", "marks": 85},
    102: {"name": "Neha", "marks": 90}
}

print(Students)
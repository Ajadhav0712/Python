# Input List = [10, 20, 30, 40]
# Search = 30
# Expected Output 30 found at index 2



list1 = [10, 20, 30, 40]

search = 30

for index, x in enumerate(list1):
    if x == search:
        print(f'{search} found at index {index}')
# Inverted Right Half Pyramid Pattern
num = 1
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
        if num > 9:
            num = 1
    print()
# set-a
# Inverted Right Half Pyramid Pattern

rows = 5
num = 1

for i in range(rows):
    for j in range(rows - i):
        print(num, end=" ")
        num += 1
        
        # Reset number after 9
        if num == 10:
            num = 1
    print()
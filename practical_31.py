# Inverted Right Half Pyramid
# Updated by Dhruv
rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Practical 4B code 
num = 1

for i in range(1, 6):      
    for j in range(i):     
        print(num, end=" ")
        
        num += 1
        
        if num == 10:      
            num = 1
            
    print()                
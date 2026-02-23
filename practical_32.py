rows = 5

for i in range(1, rows + 1):
    
    # Print spaces (for alignment)
    print(" " * (rows - i), end="")
    
    # Print stars
    for j in range(i):
        print("* ", end="")
    
    print()
# Practical 4B
for i in range(5, 0, -1):        
    for j in range(i):           
        print(chr(65 + j), end=" ")
    print()                      
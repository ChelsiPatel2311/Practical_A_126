rows = 5

for i in range(1, rows + 1):
    
    # Print spaces (for alignment)
    print(" " * (rows - i), end="")
    
    # Print stars
    for j in range(i):
        print("* ", end="")
    
    print()
# Practical 4B
rows = 5

for i in range(rows):
    # Print leading spaces
    print(" " * i, end="")
    
    # Print letters
    for j in range(rows - i):
        print(chr(65 + j), end=" ")
    
    print()                      
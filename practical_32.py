rows = 5

for i in range(1, rows + 1):
    
    # Print spaces (for alignment)
    print(" " * (rows - i), end="")
    
    # Print stars
    for j in range(i):
        print("* ", end="")
    
    print()
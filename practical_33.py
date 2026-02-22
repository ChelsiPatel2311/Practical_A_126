# Find all odd numbers between 1 to 100

odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print("List of odd numbers:", odd_numbers)
print("Minimum odd number:", min(odd_numbers))
print("Maximum odd number:", max(odd_numbers))
print("Total (Sum) of odd numbers:", sum(odd_numbers))
# Using break statement
print("Using break statement:")
for i in range(1, 11):
    if i == 6:
        break  # Exit the loop when i equals 6
    print(i, end=" ")  # Print numbers from 1 to 5

# Using continue statement
print("\n\nUsing continue statement:")
for j in range(1, 11):
    if j % 2 == 0:
        continue  # Skip even numbers
    print(j, end=" ")  # Print only odd numbers

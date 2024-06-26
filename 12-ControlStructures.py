# If statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
#FOR LOOP 
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# Variable to store the sum
sum = 0

# Iterate over the list
for val in numbers:
    sum = sum + val

# Print the sum
print("The sum is", sum)

# For loop with range
print("\nFor loop with range:")
for i in range(1, 6):  # Loop from 1 to 5 (inclusive)
    print(i)
# Nested if statement
x = 10
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is not positive")

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# Initialize a counter variable
i = 0

# While loop with a condition that checks if i is less than 5
while i < 5:
  # Print the current value of i
  print(i)
  # Increment i by 1 after each iteration
  i += 1

# Optional: Print a message after the loop finishes
print("Loop finished!")

# Function definition
def greet(name):
    print("Hello,", name)

# Function call
print("\nFunction call:")
greet("Alice")

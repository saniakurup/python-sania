# If statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For loop with range
print("\nFor loop with range:")
for i in range(1, 6):  # Loop from 1 to 5 (inclusive)
    print(i)

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# Function definition
def greet(name):
    print("Hello,", name)

# Function call
print("\nFunction call:")
greet("Alice")

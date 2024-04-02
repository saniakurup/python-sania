# Function definition
def greet():
    """This function greets the user."""
    print("Hello, world!")

# Function call
greet()

# Function with parameters
def greet_with_name(name):
    """This function greets the user with the provided name."""
    print("Hello,", name)

# Function call with parameter
greet_with_name("Alice")

# Function with default parameter
def greet_with_default(name="Guest"):
    """This function greets the user with the provided name, defaulting to 'Guest'."""
    print("Hello,", name)

# Function call without specifying parameter
greet_with_default()

# Function call with parameter
greet_with_default("Bob")

# Function with return value
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

# Function call with return value
result = add(3, 5)
print("Result of addition:", result)

# Function with multiple return values
def divide(dividend, divisor):
    """This function divides two numbers and returns the quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Function call with multiple return values
quotient, remainder = divide(10, 3)
print("Quotient:", quotient)
print("Remainder:", remainder)

# Arithmetic operators
a = 10
b = 3
print("Arithmetic operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation

# Comparison operators
x = 5
y = 8
print("\nComparison operators:")
print("x < y is", x < y)  # Less than
print("x > y is", x > y)  # Greater than
print("x == y is", x == y)  # Equal to
print("x != y is", x != y)  # Not equal to
print("x >= y is", x >= y)  # Greater than or equal to
print("x <= y is", x <= y)  # Less than or equal to

# Logical operators
p = True
q = False
print("\nLogical operators:")
print("p and q is", p and q)  # Logical AND
print("p or q is", p or q)  # Logical OR
print("not p is", not p)  # Logical NOT

# Assignment operators
x = 10
print("\nAssignment operators:")
x += 5  # Equivalent to x = x + 5
print("x += 5 (addition assignment) gives x =", x)
x -= 3  # Equivalent to x = x - 3
print("x -= 3 (subtraction assignment) gives x =", x)
x *= 2  # Equivalent to x = x * 2
print("x *= 2 (multiplication assignment) gives x =", x)
x /= 4  # Equivalent to x = x / 4
print("x /= 4 (division assignment) gives x =", x)

# Identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("\nIdentity operators:")
print("a is b is", a is b)  # is: returns True if both variables point to the same object
print("a is c is", a is c)
print("a is not c is", a is not c)  # is not: returns True if both variables point to different objects

# Membership operators
my_list = [1, 2, 3, 4, 5]
print("\nMembership operators:")
print("2 in my_list is", 2 in my_list)  # in: returns True if the value is present in the sequence
print("6 not in my_list is", 6 not in my_list)  # not in: returns True if the value is not present in the sequence

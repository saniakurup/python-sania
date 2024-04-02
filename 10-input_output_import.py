# Input/output operations
name = input("Enter your name: ")  # Input operation to get user's name
age = int(input("Enter your age: "))  # Input operation to get user's age (converted to integer)

print("Hello, " + name + "!")  # Output operation to greet the user
print("You are", age, "years old.")  # Output operation to display the user's age

# Importing modules
import math  # Importing the math module

radius = float(input("Enter the radius of a circle: "))  # Input operation to get the radius of a circle (converted to float)

area = math.pi * radius ** 2  # Calculating the area of the circle using the math module
print("The area of the circle is:", area)  # Output operation to display the area of the circle

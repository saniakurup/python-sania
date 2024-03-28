# Variable assignment
x = 10
y = 20
name = "Alice"
is_student = True

# Variable reassignment
x = 15

# Printing variables
print("Value of x:", x)
print("Value of y:", y)
print("Name:", name)
print("Is student?", is_student)

# Variable types
print("Type of x:", type(x))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))

# Variable scope
def my_function():
    z = 30
    print("Value of z inside function:", z)

my_function()
# print("Value of z outside function:", z)  # This line will raise an error because z is not defined outside the function

# Global variables
global_variable = 100

def another_function():
    global global_variable
    global_variable += 1
    print("Value of global_variable inside function:", global_variable)

another_function()
print("Value of global_variable outside function:", global_variable)

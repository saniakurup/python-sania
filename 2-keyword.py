# Python code using keywords

# Variable assignment
x = 10

# Conditional statement using 'if', 'elif', and 'else'
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# Loop using 'for' and 'range'
for i in range(5):
    print(i)

# Function definition using 'def'
def greet(name):
    print("Hello,", name)

# Function call
greet("Alice")

# List creation and manipulation using 'list' and 'append'
my_list = [1, 2, 3]
my_list.append(4)
print("List after appending:", my_list)

# Dictionary creation and accessing using 'dict' and 'keys'
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Value corresponding to 'b':", my_dict['b'])

# Class definition using 'class'
class MyClass:
    def __init__(self, x):
        self.x = x

    def display(self):
        print("Value of x:", self.x)

# Object creation and method call
obj = MyClass(5)
obj.display()

Certainly! Below is a Python script that demonstrates reading from and writing to files using file input/output operations:

```python
# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a Python script.\n")
    file.write("Writing to a file using Python File I/O.\n")

# Reading from a file
with open("output.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)

# Appending to a file
with open("output.txt", "a") as file:
    file.write("Appending additional content to the file.\n")

# Reading from the file after appending
with open("output.txt", "r") as file:
    content = file.read()
    print("\nContent of the file after appending:")
    print(content)
```

In this script:

- We first write some content to a file named "output.txt" using the `"w"` mode, which opens the file for writing. If the file already exists, its contents are overwritten. If the file doesn't exist, a new file is created.
- We then read the contents of the file using the `"r"` mode, which opens the file for reading.
- Next, we append additional content to the file using the `"a"` mode, which opens the file for appending. If the file doesn't exist, a new file is created.
- Finally, we read the contents of the file again to see the changes after appending.

Make sure to run this script in a directory where you have write permissions to create and modify files. This script demonstrates basic file input/output operations in Python.

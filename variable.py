""""
variables are containers for storing data values.
python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""

x = "Kavya"
print(x)
y = "gummadi"
print(y)
print(x+y)
print(x+" "+y)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
a = int(3)
print(a)
b = float(5)
print(b)
c = str(4)
print(c)
d = bool(1)
print(d)
e = bool(0)
print(e)
"""
Python - Variable Names
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# Camel Case: Each word, except the first, starts with a capital letter.  myVariableName = "John"
# Pascal Case: Each word starts with a capital letter.  MyVariableName = "John"
# Snake Case: Each word is separated by an underscore character.  my_variable_name = "John"

# Many Values to Multiple Variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables:
# In the print() function, you output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables.
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Global Variables:
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
# If you create a variable with the same name inside a function, this variable will be local, and can only be used
# inside the function. The global variable with the same name will remain as it was, global and with the original value.

a = "awesome"
def myfunc():
  a = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# Global Keyword:
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)














































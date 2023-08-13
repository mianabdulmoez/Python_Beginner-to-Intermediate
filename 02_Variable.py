# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)




# Types of multi variables name
# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"




# Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables 
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)






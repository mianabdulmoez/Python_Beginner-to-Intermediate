from re import A


def myfn():
    global a
    a = "hello boi"
myfn()
print(a + " How are you")

# If you create a variable with the same name inside a function, 
# this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, 
# global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# If you use the global keyword, the variable belongs to the global scope:
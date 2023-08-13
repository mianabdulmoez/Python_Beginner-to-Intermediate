# Booleans represent one of two values: "True or False".
print(9<10)
print(9>10)
print(9 == 10)
a= 500
b= 200
if a>b:
    print("yes A is greater than B")
else:
    print("B is not greater than A")
    
# Evaluate Values and Variables
x="Hello"
y=15
print(bool("x"))
print(bool(y ))

# Most Values are True
# Boolean values are true most of the time 
# But it also depend on the statement

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are false depend on the situation or statement
# In fact, there are not many values that evaluate to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None.
# And of course the value False evaluates to False.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from
#a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())
# 
def myFunction1() :
  return True

if myFunction1():
  print("YES!")
else:
  print("NO!")
#isinstance in boolean
r = 200
print(isinstance(r, int))

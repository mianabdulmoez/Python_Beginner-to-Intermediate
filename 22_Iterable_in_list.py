# ITERABLE
#The iterable can be any iterable object, like a list, tuple, set etc.
#You can use the 'range()' function to create an iterable:
list = [i for i in range(10)]
print(list)

# now using condition in iterables
list1 = [i for i in range (10) if i < 5]
# so the condition is true because 10 is lesser to 5
print(list1)

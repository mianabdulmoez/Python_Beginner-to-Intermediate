# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# slicing always  start from 0 zero
# Simple Slicing
b = "Hello, World!"
print(len(b))
print(b[2:5])
# Slice From the Start
b = "Hello, World!"
print(b[:5])#If we did'nt add 0 in it then python already include 0 in starting
# Slice To the End 
b = "Hello, World!"
print(b[7:])#It show after from the 7th word
# Negative Indexing
# In negative slicing the counting starts from -1 to etc
b = "Hello, World!"
print(b[-5:-2])
print(b[-6:-1])
# Note 
# if the  slicing is like that[7:0] or [-1:-6] 
# It c ant be print any result these are going in to smaller values


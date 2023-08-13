# Escape Sequence Character


# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# a = "I" am "Abdul moeez"  It show me error
a= "I\"am\"Abdulmoeez"
print(a)
b = "I \tam \nAbdul \tMoeez"
print(b)
# Here is some important Escape Character which are mostly use:and their work
# Single Quote
txt = 'It\'s alright.'
print(txt) 
# Backslash
txt1 = "This will insert one \\ (backslash)."
print(txt1) 
# New Line
txt2 = "Hello\nWorld!"
print(txt2) 
# Carriage Return
txt3 = "Hello\rWorld!"
print(txt3) 
# Tab
txt4 = "Hello\tWorld!"
print(txt4)  
# Backspace
#This example erases one character (backspace):
txt5 = "Hello \bWorld!"
print(txt5) 
# Hex Value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# \f	Form Feed	
# \ooo	Octal value	






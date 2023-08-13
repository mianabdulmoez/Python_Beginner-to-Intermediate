# Assign String to a Variable
a ="Hello"
a ='Hello'
# Both of these are same 
# Multiline Strings
b = """Hello
how are you
how can I help you"""
print(b) 
z="Hello\r\nhow are you\r\nhow can i help you"
print(z)
# Strings are array
c="Abdul Moeez"
print(c[0])
print(c[10])
print(c[0:10])
# Looping through strings
for x in "banana":
  print(x) 
for p in "Abdul Moeez":
    print(p)
# String lenght
print(len(p))#It show the lenght 1 bec ause of for loop
print(len(c))


# Checking of the string
# In which py check that word is in string or not
txt = "The best things in life are free!"
print("free" in txt)
k="Abdul Moez"
print("A" in k)
print("Moeez" in a) # It show the false  because of Moeez instead  of Moez
# Check if NOT
# To check if a certain phrase or character is NOT present in a string
txt = "The best things in life are free!"
print("expensive" not in txt) #it show TRUE because "expensive" is not in this string

a_z="Abdul Moeez"
print("Moeez" not in a_z)#It show false because "Moeez" is in that string
print("Mian" not in a_z)#It show TRUE because "Mian" is not in this string
txt1 = "The best things in life are free!"
if "expensive" not in txt1:
  print("No, 'expensive' is NOT present.")


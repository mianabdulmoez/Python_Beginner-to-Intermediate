# Using loop in list in shorter way
# No 1 method for comprehension
list = ["apple", "banana", "orange", "mango"]

[print(x) for x in list]
# with out if statement
list = ["apple", "banana", "mango"]
listing = [x for x in list]
print(listing)
# no 2 
# with out comprehension
list = ["apple", "banana", "orange","melon", "mango", "Kiwi"]
new_list=[]
for x in list:
     if "a" in x:
         new_list.append(x)
print(new_list)
# Now using for it comprehension method
#syntax=[expression for item in iterable if condition == True]
list = ["apple", "banana", "orange","melon", "mango", "Kiwi"]
newlist = [x for x in list if 'e' in x]
print(newlist)

# Using condition in comprehension
# here i'm using not equal != condition mean instead fo item.
list = ["apple", "banana", "orange","melon", "mango", "Kiwi"]
list1 = [x for x in list if x != 'apple']
#It print list instead of apple
print(list1)
list2 = [x for x in list if x == 'apple']
#It just print apple because condition is true for apple instead other items 
print(list2)
# Expression
list = ["apple", "banana", "orange","melon", "mango", "Kiwi"]
lister = [x.upper() for x in list]
print(lister)

# now replacing list items with single word
list = ["apple", "banana", "orange","melon"]
lister1 = ['ABDUL MOEZ' for x in list]
#it print mine in list instead of its items
print(lister1)
# expression using a condition
fruits = ["apple", "orange", "cherry", "kiwi", "mango"]
new = [x if x != "orange" else "banana" for x in fruits]
print(new)
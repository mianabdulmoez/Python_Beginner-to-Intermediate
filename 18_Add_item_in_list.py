# Insert Items
list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list1.insert(1,"Nofil")#It add on no 1
list1.insert(3,"Awais") #After inserting nofil the length is change
print(list1)

#Append Item
# To add item in the end of list use .apoend 
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list.append("Guava")
print(list)

# Extend List
# Use to add lists
thislist = ["apple", "banana", "cherry", "orange"]
list1 = ["Ali","Dawood","Hamza","Usman"]
list1.extend(thislist)
print(list1)

# Add any iterable
# you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry", "orange"]
tuple = ("Kiwi","Mango")
thislist.extend(tuple)#This is Tuple
print(thislist)
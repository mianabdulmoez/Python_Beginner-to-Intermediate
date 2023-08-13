# Remove item from list

# Remove specified Item
list = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list.remove("Ali")
# list.remove("Ali","Kareem") It cant be remove bcz these are 2
print(list)

# Remove Specified Index
#Removing specific item from index number which is pop() method
list = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list.pop(2)
print(list)
# To last item from list
list = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list.pop()
print(list)

# use del to remove
list = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
del list[2]#It remove hamza
print(list)

# To Delete the entire list 
list = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
del list
print(list) #It just show the type of list

# Clear the list
list = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list.clear()#It clear the list items
print(list)
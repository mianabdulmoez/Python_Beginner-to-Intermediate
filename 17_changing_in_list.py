# Change items in list
# Insert New Value witout replacing
list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list1.insert(1,"Nofil")#It add on no 1
list1.insert(3,"Awais")
print(list1)
# Replace
list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]  #String
list1[6]="Qazi"#It replace with Kareem
print(list1) 

# Change a range of item value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

list4 = ["ALi",1,True,"Nice,",False,46] #Mix types
list4[0:2] = ["Ameer",5]
print(list4)

# Inserting new more items then replacing 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:1] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[2:3] = ["blackcurrant", "watermelon"]
print(thislist)

list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list1[2:3] = ["Hashir","Nofil","Huzaifa"]#it replace with Hamza
print(list1)
# The length will also change after inserting more value
print(len(list1))

# Insert less value by replacing more values
list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]
list1[2:7] = ["Farhan"] #replace from Hamza to Kareem
# Inserting 1 name by replacing 5 names
print(list1)


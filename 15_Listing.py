# python array collection
#List => collection of ordered which is changeable : Allow duplicate members(copy)
#Tuple => collection of ordered which is un-changeable : Allow duplicate members(copy)
#set => collectin of un-ordered & un-changeacle & unindexed : No duplication
# Dictionary => collection of ordered & changeable : No duplicate member

# list are used to store multiple items in a single variable
# List is 1 over 4th built in data type in python
# Lists are created using square brackets : []
this_list=["Apple","bannana","Cherry","Guava","Mango"]
print(this_list)
# List length
print(len(this_list))
# List can be any data type
list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]  #String
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]  #Integer
list3 = [True, False, True, False, False, False, True, True, False] #Boolean
print(list1,list2,list3)
list4 = ["ALi",1,True,"Nice,",False,46]
print(list4)
# print(len(list1,list2,list3,list4))It show me error
print(len(list1))
print(len(list2))
print(len(list3))
print(len(list4))
# List Data type
# From python prespective list are object with list data-type
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

# List Constructor
c_list = list(("apple","bannana","mango"))
print(c_list)


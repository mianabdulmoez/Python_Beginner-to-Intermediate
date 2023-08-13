# Access of list item
# we can access list item by using index number (indexing)

list1 = ["Ali","Dawood","Hamza","Usman","Noman","Rehman","Kareem"]  #String
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]  #Integer
list3 = [True, False, True, False, False, False, True, True, False] #Boolean
list4 = ["ALi",1,True,"Nice,",False,46] #Mix types
# Indexing always start from 0
print(list1[0])
print(list1[1])
print(list1[5])
# print(list1[7])
print(list1[6])

# Negative Indexing
print(list1[-1])
print(list1[-6])
print(list1[-7])

# Range Indexing
# The last number in indexing is not count[0:5] means 0-4
# When specifying a range, the return value will be a new list with the specified items.
print(list1[1:6])
print(list1[0:4])

print(list1[:])
print(list1[0:])
print(list1[:6])
print(list1[:3])

# Negative Indexing
print(list1[-6:-1])
print(list1[-7:-1])
print(list1[-7:0])

# Checking Item in list
if 46 in list1:
    print("Yes, It is in list1")
else:
    print("No,It is not in list1")
if 46 in list2:
    print("Yes, It is in list2")
else:
    print("No,It is not in list2")
if 46 in list3:
    print("Yes, It is in list3")
else:
    print("No,It is not in list3")
if 46 in list4:
    print("Yes, It is in list4")
else:
    print("No,It is not in list4")
# user aey aur input value dy aur khudhi uss list ka name ajy jis mein wo value mojood ho
# statements ko use krty howy bnana hai elif bhi use hogi
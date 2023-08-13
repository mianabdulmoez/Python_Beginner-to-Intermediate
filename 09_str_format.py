# We cannot combine string and integer
# But theri is a format() method to combine them:let's  see
q = 500
r = "Yes he bought it for {} dollars"
print(r.format(q))
# The format() method takes unlimited number of arguments
w = "this watch"
x = "Yes he bought {} it for {} dollars"
print(x.format(w,q))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item no {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3#  0 no value
itemno = 567#  1 no value
price = 49.95# 2 no value
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
#It just using index mean start from 0
print(myorder.format(quantity, itemno, price))

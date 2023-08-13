# Assignment operators
# Identity operators
# Membership operators
# Bitwise operators

# Python Assignment Operators
#  =	        x = 5	                        x = 5
a = 5
print(a)
#  +=	    x += 3	                    x = x + 3	
b = 5
b += 3
print(b)
#  -=	    x -= 3	                    x = x - 3	 
c = 5
c -= 3
print(c)
#  *=	    x *= 3	                    x = x * 3	
d = 5
d *= 3
print(d)
#  /=	    x /= 3	                    x = x / 3	
e = 5
e /= 3
print(e)
#  %=	    x %= 3	                    x = x % 3	
f = 5
f%=3
print(f)#so its mode is 2 which remained from reminder
#  //=	    x //= 3	                    x = x // 3	
g = 5
g//=3
print(g)
#  **=	    x **= 3	                    x = x ** 3	
h = 5
h **= 3
print(h)
#  &=	    x &= 3	                    x = x & 3	
i = 5
i &= 3
print(i)
#  |=	    x |= 3	                    x = x | 3	
j = 5
j |= 3
print(j)
#  ^=	    x ^= 3	                    x = x ^ 3	
k = 5
k ^= 3
print(k)
#  >>=	    x >>= 3	                    x = x >> 3	
l = 5
l >>= 3
print(l)
# l accepter  <<=	    x <<= 3	                    x = x << 3
x = 5 
x <<= 3
print(x)
# Python Identity Operators
# is 	    Returns True if both variables are the same object	        x is y	
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not	Returns True if both variables are not the same object	    x is not y
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Python Membership Operators
# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
x = ["apple", "banana"]
print("banana"  not in x)
# returns True because a sequence with the value "pineapple" is not in the list


#  Bitwise Operator
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
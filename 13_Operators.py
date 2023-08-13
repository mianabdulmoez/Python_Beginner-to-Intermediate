# Python divides the operators in the following groups:

# Arithmetic operators
# Comparison operators
# Logical operators


#Python Arithmetic Operators
#  + 	Addition	            x + y	
print(10+8)
#  - 	Subtraction	            x - y	
print(90-80)
#  * 	Multiplication	        x * y	
print(5*3)
#  **   exponentiation is also a power 2**5
print(5**3)
#  /	Division                 x / y
print(9/2)
#  //	Floor division	         x // y  
print(9//2)
#  % 	Modulus	    x % y  =  It is also a mode
print(10%3)             # 3x3 is 9 so 1 is left 



# # Comparison operators
#  ==	    Equal	                        x == y	
a = 89
b = 67
print( a == b )
#  !=	    Not equal	                    x != y	
print( a != b )
#  >	    Greater than	                x > y	
print( a > b )
#  <	    Less than	                    x < y	
print( a < b )
#  >=	    Greater than or equal to	    x >= y	
print( a >= b )
#  <=	    Less than or equal to	        x <= y
print( a <= b )

# Logical operators
#  and  Returns True if both statements are true	                  x < 5 and  x < 10	
x = 50
print(x > 30 and x < 100)
print(x > 100 and x < 40)
#  or	Returns True if one of the statements is true	              x < 5 or x < 4	
print(x > 40 or x < 30)
print(x > 60 or x < 30)
print(x > 40 or x < 60) # its true
#  not	Reverse the result, returns False if the result is true	not  (x < 5 and x < 10)
print(not(x > 40  and x < 60))
print(not(x > 80  and x < 10))

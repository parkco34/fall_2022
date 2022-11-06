#Calculations test script
#author : Kevin Soule
#date 8/25/2017


valueA = 5
valueB = 13
floatC = 12.5
stringD = "Hello"
stringE = "World"

#Use variables or numbers with operators
print("Part 1")
valueA + valueB
3/5
valueA ** 10    #python happily does the math but result goes?
print()
############################################################

print("Part 2") # outputs to simple equations
print(15 + valueA)
outcome = valueA * valueB
print(outcome)
print(stringD + "class") #Note : Plus operator works with strings
print(stringD,"class") #automatic separator for multiple outputs
print()
############################################################

print("Part 3") # operator precedence in larger equations

#Order of operations in python
##1.  exponents
##2.  multiplication,divsion, and remainder
##3.  addition and subtraction
# Any tie between operations on precedence level goes left to right
# Assignments to variables have the lowest precedence

result1 = 4 + 8 / 2
result2 = (4 + 8) / 2
print("Result1 = " , result1, "   Result2 = ",result2)
# This illustrates using parathesises to change precedence if needed
# Use of parathesises even if not needed is not a problem
print()
#############################################################

print("Part 4") # division versus integer division

#  "/" and "//" are division operators
# "/" is regular division but all results are in float
# "//" all results are integer , any values after decimal pt cut off

print( "13/5 = ", 13/5)
print( "15/5 = ", 15/5)
print( "13//5 = ", 13//5)
print( "15//5 = ", 15//5)
print()
#############################################################

print("Part 5") # remainder operator

# When using int division sometimes it is important to keep the remainder
print( "17%6 = ", 17%6)
print()
#############################################################

print("Part 6") # exponent operator

# to do exponents we use the ** operator
print("7**2 = " , 7**2)
print()
#############################################################

print("Part 7") # mixed int and float in equations

#Python has rules on how to handle calculations becuase the result
#has to be stored as a certain type
##1. If both operands are int or float than that is the result
##2. If one operand is an int and one a float the result is float
print("4 * 2.5 = " , 4 * 2.5)

#we can always convert between types if we need the result to be different
print("int(4 * 2.5) = " , int(4 * 2.5))

#float() and str() functions are also available should we need them
print()
#############################################################

print("Part 8") # line continuation 
#If equation is too long for line we can use the line continuation operator
# '\' operator at end of line

result3 = valueA * valueB * (floatC / result1) /  \
          valueA + valueB
print(result3)

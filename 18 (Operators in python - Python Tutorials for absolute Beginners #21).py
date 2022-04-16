# Operators in python
#   1. Arithmetic Operators
#   2. Assignment Operators
#   3. Comparison Operators
#   4. Logical Operators
#   5. Identity Operators
#   6. Membership Operators
#   7. Bitwise Operators


#########################################################
# Arithmetic Operators
print("Arithmetic Operators")

print("5 + 6 is", 5 + 6) # here the output is 5 + 6 is 11
print("5 - 6 is", 5 - 6) # here the output is 5 - 6 is -1
print("5 * 6 is", 5 * 6) # here the output is 5 * 6 is 30
print("5 / 6 is", 5 / 6) # Here the output is 5 / 6 is 0.8333333333333334
print("5 // 6 is", 5 // 6) # here the output is 5 // 6 is 0    # // it basically return a int value after divide
print("15 // 6 is", 15 // 6) # Here the output is 15 // 6 is 2
print("5 ** 3 is", 5 ** 3) # Here the output is 5 ** 3 is 125    # ** mens for example 5*5*5
print("5 % 3 is", 5 % 3)  # Here the output is 5 % 3 is 2   # it also basically return remainder
print("5 % 5 is", 5 % 5)  # here the output is 5 % 5 is 0   # it also basically return remainder



# Assignment Operators
# it is basically use when we want to assign a value to a variable
print("Assignment Operators")

x = 5 # here = is an Assignment Operator
print(x) # here output is 5

x += 7  # here += is also a Assignment Operators  # x += 7  ----->  x = x + 7
print(x) # here output is 12

x -= 5  # here -= is also a Assignment Operators  # x -= 5  ----->  x = x - 5
print(x) # here output is 7

x *= 7   # here *= is also a Assignment Operators  # x *= 7  ----->  x = x * 7
print(x) # here output is 49

x /= 7 # here /= is also a Assignment Operators  # x /= 7  ----->  x = x / 7
print(x) # here output is 7.0

x %= 5  # here %= is also a Assignment Operators  # x %= 7  ----->  x = x % 7
print(x) # here output is 2.0



# Comparison Operators
print("Comparison Operators")

i = 8
print(i == 5) # here output is false  # This are the example of Comparison Operators

print(i == 8) # here the output is True  # This are the example of Comparison Operators

print(i != 5) # here output is True  # This are the example of Comparison Operators

print(i > 8) # here output is False  # This are the example of Comparison Operators

print(i >= 8) # here output is True  # This are the example of Comparison Operators

print(i <= 8) # here output is True  # This are the example of Comparison Operators



# Logical Operators
print("Logical Operators")

a = True
b = False

print(a and a) # here the output is True because both are True

print(a and b) # here the output is True because both are False

# *** and operator can only return true when both are true


print(a or b) # here the output is True because both are True


#|-----------------------------------|---------------------------------------|
#        and Operators               |            or Operators               |
#----------------------------------------------------------------------------|
# when both are true                 | when anyone is true                   |
#------------------------------------|---------------------------------------|




# Identity Operators
print("Identity Operators")

print(a is b) # here output is False   # because a is true and b is false

print(a is not b) # here output is True   # because a is true and b is false

print(5 is not 7) # here output is True   # because 5 & 7 are not same

print(5 is not 5) # here output is false   # because 5 & 5 are same




# Membership Operators
print("Membership Operators")

list = [3, 3, 2, 3, 33, 35, 32]
print(32 in list)  # output is True because 32 is present in list

print(324 in list)  # output is False because 324 is not present in list

print(324 not in list)  # here output is True because here we use not in



# Bitwise Operators
print("Bitwise Operators")
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 1) # output 0
print(0 | 1) # output 1
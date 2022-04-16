#Python list and list Function
grocery = ["Vim bar", "Bhindi", "Lollypop", "Chitrajyoti", "Arijit"]
print(grocery) # Here the output is ['Vim bar', 'Bhindi', 'Lollypop', 'Chitrajyoti', 'Arijit']

grocery1 = ["Vim bar", "Bhindi", "Lollypop", "Chitrajyoti", "Arijit", 56]
print(grocery1) # Here the output is ['Vim bar', 'Bhindi', 'Lollypop', 'Chitrajyoti', 'Arijit', 56]
print(grocery1[0]) # Here the output is Vim bar
print(grocery1[1]) # Here the output is Bhindi
print(grocery1[2]) # Here the output is Lollypop
print(grocery1[3]) # Here the output is Chitrajyoti
print(grocery1[4]) # Here the output is Arijit
print(grocery1[5]) # Here the output is 56
#print(grocery[6]) # If we wright this line it will be thhrough a error

number = [2, 1, 9, 11, 3]
print(number) # Here the output is [2, 1, 9, 11, 3]
print(number[0]) # Here the output is 2
print(number[1]) # Here the output is 1
print(number[2]) # Here the output is 9
print(number[3]) # Here the output is 11
print(number[4]) # Here the output is 3

# If we want to do just like this { smaller vale -----> higher value } then
number.sort()
print(number)  # Here the output is [1, 2, 3, 9, 11]

# if we want wright value reverse side then
number.reverse()
print(number) # Here the output is [11, 9, 3, 2, 1]


# In python List slicing is similar to String Slicing
# ***** print(abc[starting index value --> by default 0 : index value of list upto end( by default : skip])
number1 = [2, 1, 9, 11, 3]
print(number1[0:5]) # Here the output is [2, 1, 9, 11, 3]
print(number1[:5])  # Here the output is [2, 1, 9, 11, 3]
print(number1[:])   # Here the output is [2, 1, 9, 11, 3]
print(number1[1:])  # here the output is [1, 9, 11, 3]
print(number1[1:4]) # Here the output is [1, 9, 11]
print(number1[::1]) # Here the output is [2, 1, 9, 11, 3]
print(number1[::2]) # Here the output is [2, 9, 3]
print(number1[::3]) # Here the output is [2, 11]
print(number1[::-1]) # Here the output is [3, 11, 9, 1, 2]
print(number1[::-3]) # Here the output is [3, 1]

print(number1[1:5:-3]) # Here the output is []
# **** Please don't take negative Slicing. Ex.- print(number1[1:5:-3])

print(number1[1:5:3]) # Here the output is [1, 3]

print(len(number1)) # Here the output is 5
print(max(number1)) # Here the output is 11
print(min(number1)) # here the output is 1

# *** if we want to add some value after the value stored in list then.
# Mens ex. number1 = [2, 1, 9, 11, 3,]
# after using append ----->  number1 = [2, 1, 9, 11, 3, value of append]

number1.append(71)
print(number1) # Here the output is [2, 1, 9, 11, 3, 71]

number1.append(77)
print(number1) # Here the output is [2, 1, 9, 11, 3, 71, 77]

number1.append(73)
print(number1) # Here the output is [2, 1, 9, 11, 3, 71, 77, 73]


# now we will create a blank list which will be filled by append
numbers = []
numbers.append(71)
numbers.append(72)
numbers.append(73)
print(numbers) # Here the output is [71, 72, 73]



# Insert
# By insert we can insert value in any index value
# For example we want to add 67 at index value 1 then the code will be number1.insert(1, 67)

number1.insert(1, 67)
print(number1) # Here the output is [2, 67, 1, 9, 11, 3, 71, 77, 73]

number1.insert(3, 67)
print(number1) # here the output is [2, 67, 1, 67, 9, 11, 3, 71, 77, 73]



# remove
# if we want to remove spacific value from list then we will use remove

number1.remove(9)
print(number1) # Here the output is [2, 67, 1, 67, 11, 3, 71, 77, 73]


# Pop
# We use pop when we need to remove a value of list from the last
# Example. list =[2, 67, 1, 67, 11, 3, 71, 77, 73]
# but if we run pop then the output will be [2, 67, 1, 67, 11, 3, 71, 77]

number1.pop()
print(number1) # Here the output is [2, 67, 1, 67, 11, 3, 71, 77]



# If we want to replace a spacific value from a spacific index value then
number1[1] = 98
print(number1) # Here the output is [2, 98, 1, 67, 11, 3, 71, 77]


'''
Mutable = can change
Imutable = cannot change
'''
# tuples
# *** in tuples we can,t change value of tuples

tp = (1,2,3)
print(tp)    # Here the output is (1, 2, 3)

# tp[1] = 8   # We can't write this line because we can,t change the the value of tuples

tp1 = (1)
print(tp1) # Here the output is 1

tp2 = (1,)
print(tp2) #  Here the output is (1,)

# if we want to inter change the value mens want to assign a's value into b and b's value into a
a = 1
b = 8
temp = a
a = b
b = temp
print(a, b)

# **** if we want to inter change the value mens want to assign c's value into d and d's value into c
# **** but if we want to do it it by using python it will be much easyer
c = 18
d = 20
c,d = d,c
print(c,d)
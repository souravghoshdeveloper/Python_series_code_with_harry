# function
a = 9
b = 8
c = sum((a,b)) # built in Function
print(c)

# user define function
def function1():
    print("Hello You are in Function 1")

#print(function1())
# here the output is Hello You are in Function 1
#                    None

function1() # here the output is Hello You are in Function 1


##############################################################
# if we just run this code --->function1()  multiple time then we got the output ---> Hello You are in Function 1

function1() # here the output is Hello You are in Function 1
function1() # here the output is Hello You are in Function 1
function1() # here the output is Hello You are in Function 1
function1() # here the output is Hello You are in Function 1
function1() # here the output is Hello You are in Function 1



##############################################################
def function2(d, e):
    print("Hello you are in function 2", d + e)

function2(5, 7) # here output is Hello you are in function 2 12


##############################################################
def function3(f, g):
    average = (f + g)/2
    print(average)

function3(5, 7) # here output is 6.0



#############################################################
def function4(h, i):
    average1 = (h + i)/2
    print(average1)  # here output is 7.0
    return average1
v = function4(6, 8)
print(v)  # here output is 7.0



##############################################################
def function5(j, k):
    """This is a function which will calculate average of two numbers"""  # it is a doc string
    average3 = (j + k)/2
    print(average3)  # here output is 11.0
    return average3
u = function5(10, 12)
print(u)  # here output is 11.0
print(function5.__doc__) # output --> This is a function which will calculate average of two numbers



# another example
def function6(l, m):
    """This is a function which will calculate average of two numbers
    This function doesnot work for three numbers"""
    average2 = (l + m)/2
    print(average2)  # here output is 7.0
    return average2
t = function6(15, 17) # here output is 16.0
print(t)  # here output is 16.0
print(function6.__doc__)  # here output is This is a function which will calculate average of two numbers
#                                              This function doesnot work for three numbers
def function1(a):
    print(a, "I have printed")

function1("This is me")     # here the output is This is me I have printed




###############################################################################
# Global Variable - Global Variable is a variable which can be use in multiple function

b = 10  # Global Variable
def function2(c):
    b = 5   # local variable
    print(c, "I have printed")

function2("This is me") # output This is me I have printed
print(b) # output 10    # output is 10 because b = 10 is an global variable & b = 5 is not an global variable because it is inside this function
# Here we run --> print(b) outside of the function so here output is 10


# if we don't assign any value indsie function
d = 20  # Global Variable
def function3(e):
    #d = 5  # local variable
    print(d) # output 20    # brecause d = 20 is an global variable. if we dont assign any value inside this function then it will be take the value of global variable automatically
    print(e, "I have printed")

function3("This is me") # output This is me I have printed
print(d) # output 20


# if we assign any value inside the function & want to print this value inside this function then
f = 30  # Global Variable
def function4(g):
    f = 5   # local variable
    print(f) # output 5     # we assign f = 5 inside this function and print it inside the function
    print(g, "I have printed")

function4("This is me") # output This is me I have printed
print(f) # output 30    # because it(f = 5) is not a Global Variable & it is not accessible outside this function


# another example
h = 40  # Global Variable
def function5(i):
    h = 7   # local variable
    j = 9   # local variable
    print(h, j)     # output 7 9    # because h = 7 is present as local variable in this function # when we will run --> print(h ,j) then first it will be want to find is h present inide this function if it is present then it will be print the value it. if not present inside this function then it will be find for global varible
    print(i, "I have printed")

function5("This is me") # output This is me I have printed
print(h)  # output 40


# another example
k = 50  # Global Variable
def function6(m):
    k = 7   # local variable
    l = 9   # local variable
    k = k + 45
    print(k, l) # here output is 52 9   # because it add 7 + 45 for k & l was 9 so output is 52 9
    print(m, "I have printed")

function6("This is me") # output This is me I have printed
print(k)  # output 50







#########################################################################################################
# Global Keyward

# if we do like this we will got an error because we can not change the valur of global variable like this
"""
n = 60  # Global Variable
def function7(p):
    #n = 6   # local variable
    q = 8   # local variable
    n = n + 47
    print(n, q)
    print(p, "I have printed")

function7("This is me")
print(n)
"""

# if we want to change the value of global variable then
n = 60  # Global Variable
def function7(p):
    #n = 6   # local variable
    q = 8   # local variable
    global n # by using this we provide permission to change the value of global variable
    n = n + 47
    print(n, q) # output is 107 8 because here we update the value of global variable
    print(p, "I have printed")

function7("This is me")     # output This is me I have printed
print(n)   # output 107







###################################################################################################################
# *** this type of function is called nested function
"""
def sourav():
    x = 56
    def srijit():
        global  x
        x = 88
    print("before calling srijit()", x)
    srijit()
    print("after calling srijit()", x)

sourav()
"""

# *** in this function there is an misconception
# the misconception is if we use there global that does not mean it will be find x in sourav function
# here we use globle that means it will find x outside the nested function

def sourav():
    x = 56
    def srijit():
        global  x
        x = 88
    print("before calling srijit()", x)     # output before calling srijit() 56
    srijit()
    print("after calling srijit()", x)      # output after calling srijit() 56

sourav()


# if do like this
def chitrajyoti():
    y = 59
    def arijit():
        global  y
        y = 85
    print("before calling arijit()", y)     # output before calling arijit() 59
    arijit()
    print("after calling arijit()", y)      # output after calling arijit() 59

chitrajyoti()
print(y) # here the output is 85 because first it(global) will be find y in main program if there was y then it will be update the value of y & print that value but in this condiction in main program there is no y so, it will be create a global variable y & assign value 85 to it.




# Quiz
"""
# what will be output of this program
z = 99
def spandan():
    z = 33
    def srinjoy():
        global  z
        z = 44
    print("before calling srinjoy()", z)
    srinjoy()
    print("after calling srinjoy()", z)

spandan()
print(z)
"""

z = 99
def spandan():
    z = 33
    def srinjoy():
        global  z
        z = 44
    print("before calling srinjoy()", z) # output before calling srinjoy() 33
    srinjoy()
    print("after calling srinjoy()", z) # after calling srinjoy() 33

spandan()
print(z) # here the output is 44 because we update the value of z

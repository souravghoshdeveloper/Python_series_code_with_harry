#Variables
# *** we can assume variable as a bucket. Where we can store any type of data
var1 = "Hello World"  # datatype string
var2 = 4              # datatype int
var3 = 36.7           # datatype float
print(var1)
print(var2)
print(var3)
print(var1,var2,var3)

# if we want to know the type of variables
print(type(var1))
print(type(var2))
print(type(var3))

############################
print(var2+var3)
# but We can not write this type of code (print(var1+var2) or print(var1+var3)) because we can't add string with float or int

# if we want to add string with another string then
var4 = " Electrical Engineer"
print(var1 + var4)

#############################
var5 = "77" #hare the value of var5 is 77 which is a int but we don't get any error because we write here between "". So, Now 77 will be treated as String
print(var1+var5)

#############################
var6= "54 " #we write here 54 like this "54". So, it will be treated as String
var7 = "32" #we write here 32 like this "33". So, it will be treated as String
print(var6 + var7) # here the output is '54 32' because we add here two string


#*** Typecasting (When we want to change datatype for example var6 & var7 is now a string by using typecasting we want to chane datatype (string to int)
print(int(var6) + int(var7)) # here the output is 86 because here we change there(var6 & var7) datatype string to int


# if we want to print something 10 times then
print( 10 * "Hello World")
# here the output will be Hello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello World

# but we want to print each in new line then we will use a new line char.(\n)
print( 100 * "Hello World\n")

##############################
var8 = "33"
var9 = "53"
print(int(var8) + int(var9))
# if we want to print this 100 times then
print(100 * str(int(var8) + int(var9)))



# Take user input
print("Enter your name")
inputname = input()
print(inputname)
print("Your name is ", inputname)

# when we take input frm user it will alows be string
print("Enter any no.")
inputno = input()
# print(inputno + 56) #if we write this line it will give an error because the input we take from user is string
print(int(inputno) +56)


# a small quiz (here we will create a simple calculator which can only add two no. geven by user)
print("Enter first no")
firstno = input()
print("Enter second no")
secondno = input()
print("Sum of these two no. is ", int(firstno) + int(secondno))
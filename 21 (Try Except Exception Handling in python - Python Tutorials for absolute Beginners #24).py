print("Enter num 1")
num1 = int(input())
print("Enter num 2")
num2 = int(input())
print("The sum of these two numbers is",num1+num2)

######################################################
print("Enter num 3")
num3 = input()
print("Enter num 4")
num4 = input()
print("The sum of these two numbers is",int(num3)+int(num4))


############################################################
print("Enter num 5")
num5 = input()
print("Enter num 6")
num6 = input()
# in case if user give an input in char like (abcd) then we can not convert it into int in that condiction we will get an error
# as we know if we got an error then the left program will not be executed
# the soluction of this problem is Try Except Exception Handling in Python
try:
    print("The sum of these two numbers is",int(num5)+int(num6))
except Exception as e:
    print(e)

print("This line very importent")

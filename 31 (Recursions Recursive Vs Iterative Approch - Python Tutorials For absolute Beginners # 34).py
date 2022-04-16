def print2(str1):
    print("This is " + str1)

print2("Sourav") # output This is Sourav

#########################################################
# if we do like this we will get an error ---> RecursionError: maximum recursion depth exceeded
# we got this error because we use here function inside function & dont stop it
"""
def print2(str1):
    print2(str1)
    print("This is " + str1)

print2("Sourav")
"""


#######################################################
# 5! = 5*4*3*2*1
# how to calculate factorial using Recursions
# n! = n*n-1 * n-2 * n-3................1
# n! = n * (n-1)!

def factorial_iterative(n):
    """

        :param n: Integer
        :return: n*n-1 * n-2 * n-3................1
        """
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac

number = int(input("Enter the  number "))

print("Factorial using Iterative Methode",factorial_iterative(number))



########################################################################
def factorial_recursive(n):
    """

        :param n: Integer
        :return: n*n-1 * n-2 * n-3................1
        """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


    # how it works
    # for example user give ab input 5

    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)    # in this condiction --> factorial_recursive(1)  it will be run the if statement
    # 5 * 4 * 3 * 2 * 1 = 120


number = int(input("Enter the  number "))

print("Factorial using recursive Methode",factorial_recursive(number))





# quiz - fibonacci sequence calculate function
# example of fibonacci sequence --> 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the  number "))

print(fibonacci(number))
# Exercise 2 - Faulty Calculator
# 45 *3 = 555, 56+9 = 77, 56/6 = 4
# Design a  calculator which wll correctly solve all the problems except the following ones: 45 *3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as as input from the user and then retur the result

print("Enter First number")
first_number = int(input())
print("Enter operator?")
enter_operator = input()
print("Enter second number")
second_number = int(input())

if first_number == 45 and enter_operator == "*"  and second_number == 3:
    print("555")
elif first_number == 56 and enter_operator == "+" and second_number == 9:
    print("77")
elif first_number == 56 and enter_operator == "/" and second_number == 6:
    print("4")
else:
    if enter_operator == "+":
        print("Sum of this two number is",first_number + second_number)
    elif enter_operator == "-":
        print("Subtraction of this two number is",first_number - second_number)
    elif enter_operator == "*":
        print("Multiplication of this two number is",first_number * second_number)
    elif enter_operator == "/":
        print("Division of this two number is",first_number / second_number)
    else:
        print("Please enter +, -, * or /")
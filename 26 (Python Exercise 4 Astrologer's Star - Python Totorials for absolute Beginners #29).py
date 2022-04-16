# Pattern Printing
"""
Input = Integer n
Boolean = True or False

True
*
**
***
****

False
****
***
**
*
"""
print("How many Row You want to Print")
How_many_Row_You_want_to_Print = int(input())
print("Type 1 or 0")
enter_0_or_1 = int(input())
convert_into_boolean = bool(enter_0_or_1)

if convert_into_boolean == True:
    for i in range(1, How_many_Row_You_want_to_Print+1):
        for j in range(1, i+1):
            print("*",end=" ")
        print()


else:
    for i in range(How_many_Row_You_want_to_Print, 0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

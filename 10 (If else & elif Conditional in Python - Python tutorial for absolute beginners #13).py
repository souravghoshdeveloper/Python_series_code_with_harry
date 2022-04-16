var1 = 6
var2 = 56

var3 = int(input())

if var3>var2:
    print("Greter")
else:
    print("lesser")



#######################################
var4 = 77
var5 = input()
var6 = int(var5)

if var6>var4:
    print("Gretter")
elif var6==var4:
    print("Equal")
else:
    print("lesser")



#another example
var7 = 99
var8 = int(input())

if var8>var7:
    print("Gretter")
elif var8==var7:
    print("Equal")
else:
    print("lesser")


#                         |-----------------|
#-------------------------|       Note:     |-----------------------
#                         |-----------------|

# *** we can write anything we want
# -----------------------------------------------------------------|
#                                      |-----------------------|   |
#      |----------------------|        |    var5 = input()     |   |
#      |  var6 = int(input()) |    OR  |                       |   |
#      |----------------------|        |    var6 = int(var5)   |   |
#                                      |-----------------------|   |
# -----------------------------------------------------------------|




####################################################
list1 =[5, 7, 3]
if 5 in list1:    # we use here in keyword
    print("Yes its in the list")   # here output is Yes its in the list



####################################################
list2 =[5, 7, 3]
print(5 in list2)   # output true       # we use here in keyword
if 5 in list2:
    print("Yes its in the list2") # output Yes its in the list2



####################################################
list3 =[5, 7, 3]
print(15 in list3)     # we use here in keyword      # output is False
if 15 in list3:
    print("Yes its in the list3")
# here output is false



####################################################
list4 =[5, 7, 3]
print(15 not in list4)     # we use here not in keyword      # output is True
if 15 not in list4:
    print("Yes its not in the list4")    # output is Yes its not in the list4



####################################################
# Quiz:

print("Enter your age")
age = int(input())

if age > 18:
    print("You can drive")
elif age== 18:
    print("We will think about you")
else:
    print("You can't drive")



##########################################################
print("What is ypur age?")
age1 = int(input())

if age1 > 7 and age1 < 100:
    if age1 > 18:
        print("You can drive")
    elif age1 == 18:
        print("We will think about you")
    else:
        print("You can't drive")
else:
    print("Please, Enter a valid age")
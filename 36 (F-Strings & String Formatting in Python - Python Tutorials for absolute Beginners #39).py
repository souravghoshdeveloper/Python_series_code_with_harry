# F Strings & String Formatting


me = "Sourav"
a = "this is me %s"%me      # This is an example of String Formatting
print(a)                    # output --> this is me Sourav


##############################################################
me1 = "Sourav"
s1 = 3
a1 = "this is me %s %s"%(me1, s1)      # This is another example of String Formatting
print(a1)     # output --> this is me Sourav 3


#############################################################
me2 = "Sourav"
s2 = 3
a2 = "This is {} {}"
b = a2.format(me2, s2)
print(b)        # output --> This is Sourav 3



#############################################################
me2 = "Sourav"
s2 = 3
a2 = "This is {1} {0}"
b = a2.format(me2, s2)
print(b)    # output --> This is 3 Sourav


# F String
name = "Sourav"
three = 3
h = f"this is {name} {three}"   # We use here F String
print(h)    # output --> this is Sourav 3


# another example
name1 = "Sourav"
three1 = 3
g = f"this is {name1} {three1} {4 * 65}"    # We use here F String
print(g)    # Output --> this is Sourav 3 260



################################################################
import math     # as a good developer we need to write import math at the top of the program but we write it here because of ggod uder standing
name2 = "Sourav"
three2 = 3
z = f"this is {name2} {three2} {math.cos(65)}"  # We use here F String
print(z)   # Output --> this is Sourav 3 -0.562453851238172




###################################################################
# Note:
# We can add 2 or more String using + symbol but if we use F String then it will be provide a better readability

mystr = "Sourav is a good boy"
print(mystr)  # Here the output is Sourav is a good boy
print(mystr[4])  # Here the output is a because a is in 4 index in Sourav
#                                                                 012345


print(mystr[0:4])  # HEre the output is Sour because 0:4 mens index(0,1,2,3)
#                                           Sourav
#                                           012345


print(mystr[0:6])  # HEre the output is Sourav because 0:6 mens index(0,1,2,3,4,5)
#                                           Sourav
#                                           012345


print(len(mystr))  # Here the output is 20 because the length is 20 of 'Sourav is a good boy'

print(mystr[0:20])  # Here the output is Sourav is a good boy

# print(mystr[50]) # We can not Wright this because in 'Sourav is a good boy' has no value in 50 index


print(mystr[0:50]) # But we can wright this. In this condition if it has not upto 50 index then it will be be print how much it has.
#                    Here the output is Sourav is a good boy


print(mystr[0:6:2]) # Here the output is Sua. beacuse print(mystr[starting index:upto ending index:skip])
#                                        Sourav
#                                        012345
#                                        S u a


print(mystr[0:]) # Here the output is Sourav is a good boy.
# in this condition(print(mystr[0:])) it will be assumed as print(mystr[0:up to end index(by default)])


print(mystr[:6]) # Here the output is Sourav
# in this condition(print(mystr[:6])) it will be assumed as print(mystr[0 (starting index(by default)):6])


print(mystr[:]) # Here the output is Sourav is a good boy
# in this condition(print(mystr[:])) it will be assumed as print(mystr[0 (starting index(by default)):up to end index(by default)])


print(mystr[::]) # Here the output is Sourav is a good boy
# Because in this condition(print(mystr[::])) it will be assumed as print(mystr[starting index(by default):up to end index(by default):skip 1 (by default])


print(mystr[0:20:1]) # Here the output is Sourav is a good boy
# because in print(mystr[0:20:1]) mens  print(mystr[staring index:end index:skip])


print(mystr[:20:1]) # here the output is Sourav is a good boy
# because in print(mystr[:20:1]) we dont provide any starting index value in it so, it is act like print(mystr[0 (by degault starting index):20:1])


print(mystr[::1]) # here the output is Sourav is a good boy
# because in Sourav is  a     g  o  o  d     b  o  y
#            0123456789 10 11 12 13 14 15 16 17 18 19


print(mystr[::2]) # here the output is Sua sago o
# because in Sourav is  a     g  o  o  d     b  o  y
#            0123456789 10 11 12 13 14 15 16 17 18 19
#            S u a   s  a     g     o           o
# *******skip next 1 char and print


print(mystr[::3]) # Here the output is Sr  gdo
# because in Sourav is  a     g  o  o  d     b  o  y
#            0123456789 10 11 12 13 14 15 16 17 18 19
#            S  r              g        d       o
# *******skip next 2 char and print


print(mystr[::5559]) # here the output is S
# here output is only S vecause it has not enough char for skip (5559) after 0 index value (S)


print(mystr[-6:]) # Here the output is od boy
# because in S    o   u   r    a        v        i      s        a         g   o  o   d      b  o  y
#           -20 -19 -18 -17  -16      -15  -14  -13   -12  -11  -10  -9   -8  -7 -6  -5  -4 -3 -2 -1
# here we take from last. So the output is od boy                ------>          o   d      b  o  y


print(mystr[-6:-4]) # Here the output is od
# because in S    o   u   r    a        v        i      s        a         g   o  o   d      b  o  y
#           -20 -19 -18 -17  -16      -15  -14  -13   -12  -11  -10  -9   -8  -7 -6  -5  -4 -3 -2 -1
# here we take from last(-6 to -4). So the output is od          ------>          o   d


print(mystr[14:16]) # here output is od
# because in Sourav is  a     g  o  o  d     b  o  y
#            0123456789 10 11 12 13 14 15 16 17 18 19


print(mystr[::-1]) # Here the output is yob doog a si varuoS
# Here is this type os output because we use haere - symbol so, - symbol mens count from end side


print(mystr[::-2]) # Here the output is ybdo  ivro
# because in S    o   u   r    a        v        i      s        a         g   o  o   d      b  o  y
#           -20 -19 -18 -17  -16      -15  -14  -13   -12  -11  -10  -9   -8  -7 -6  -5  -4 -3 -2 -1
#                o       r             v         i                            o       d      b     y


# ************* Note: For above all program print(mystr[::]) -----> print(mystr[0 (Starting Index value(By default)):end index value:skip])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


print(type(mystr)) # Here the output is <class 'str'>

print(mystr.isalnum()) # here the Output is False

print(mystr.isalpha()) # here the Output is False

print(mystr.endswith("boy")) # Here the output is True
# Because in 'Sourav is a good boy' is end with boy

print(mystr.endswith("bdoy")) # Here the output is False
# Because in 'Sourav is a good boy' is not end with bdoy

print(mystr.count("b")) # Here the output is 1
# Because in 'Sourav is a good boy' we use b just for 1 time

print(mystr.count("o")) # Here the output is 4
# Because in 'Sourav is a good boy' we use o just for 4 time

print(mystr.capitalize()) # Here the is Sourav is a good boy
# Because we use it for capitalize the first char of a Sentence

print(mystr.find("is")) # here the output is 7
# because in 'is' is starting from 7 index value

print(mystr.lower()) # here the output is sourav is a good boy

print(mystr.upper()) # Here the output is SOURAV IS A GOOD BOY

print(mystr.replace("is", "are")) # Here the output is Sourav are a good boy
# Because we replace is by are
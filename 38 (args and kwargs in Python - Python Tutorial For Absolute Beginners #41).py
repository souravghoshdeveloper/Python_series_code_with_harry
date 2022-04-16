def function_name_print(a, b, c, d):
    print(a, b, c, d)


function_name_print("Sourav", "Chitrajyoti", "Srijit", "Arijit")    # output Sourav Chitrajyoti Srijit Arijit


###############################################################################################################
# But if we run this code code We will got an error because we provide an extra argument --> Srinjoy

# def function_name_print1(a, b, c, d):
#     print(a, b, c, d)
#
#
# function_name_print1("Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy")


##############################################################################################################
# it is a soluction but it is not the proper way to solve it
def function_name_print1(a, b, c, d, e):
    print(a, b, c, d, e)


function_name_print1("Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy")


##############################################################################################################
def funargs(*args):
    print(args[0])

sou = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy"]
funargs(*sou)   # output Sourav


##############################################################################################################
def funargs1(*args):
    print(type(args))  # utput <class 'tuple'>
    for item in args:
        print(item)

sour = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer"]
funargs1(*sour)
# output Sourav
#        Chitrajyoti
#        Srijit
#        Arijit
#        Srinjoy
#        Spandan
#        The Programmer




##############################################################################################################

def funargs2(normal, *args):
    print(normal)
    for item in args:
        print(item)

soura = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer", "Arka"]
normal = "This is a normal"
funargs2(normal, *soura)

# output This is a normal
#        Sourav
#        Chitrajyoti
#        Srijit
#        Arijit
#        Srinjoy
#        Spandan
#        The Programmer
#        Arka



# another example
def funargs3(normal, *args):
    print(normal)
    for item in args:
        print(item)

sourav = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer", "Arka", "Subham"]
normal = 34
funargs3(normal, *sourav)

# output 34
#        Sourav
#        Chitrajyoti
#        Srijit
#        Arijit
#        Srinjoy
#        Spandan
#        The Programmer
#        Arka
#        Subham



##################################################################################################
# another example
def funargs4(normal, *argschitrajyoti):
    print(normal)
    for item in argschitrajyoti:
        print(item)

sourav1 = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer", "Arka", "Subham", "Sukhen"]
normal = "I am a normal Argument and the students are:"
funargs4(normal, *sourav1)

# output I am a normal Argument and the students are:
#        Sourav
#        Chitrajyoti
#        Srijit
#        Arijit
#        Srinjoy
#        Spandan
#        The Programmer
#        Arka
#        Subham
#        Sukhen



##################################################################################################
# But we can't do like this

# def funargs5(*argschitrajyoti, normal):
#     print(normal)
#     for item in argschitrajyoti:
#         print(item)
#
# sourav1 = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer", "Arka", "Subham", "Sukhen"]
# normal = "I am a normal Argument and the students are:"
# funargs5(*sourav1, normal)





##################################################################################################

def funargs6(normal, *argschitrajyoti, **kwargs):
    print(normal)
    for item in argschitrajyoti:
        print(item)

    print("\nNow I would like to Introduce sume of our Heroes")

    for key, value in kwargs.items():
        # print(key, value)
        print(f"{key} is a {value}")

sourav2 = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer", "Arka", "Subham", "Sukhen"]
normal = "I am a normal Argument and the students are:"
kw = {"Sourav":"Programmer", "Chitrajyoti":"Fitness Instructor", "Srijit":"Coordinator"}
funargs6(normal, *sourav2, **kw)

# output I am a normal Argument and the students are:
#        Sourav
#        Chitrajyoti
#        Srijit
#        Arijit
#        Srinjoy
#        Spandan
#        The Programmer
#        Arka
#        Subham
#        Sukhen
#
#        Now I would like to Introduce sume of our Heroes
#        Sourav is a Programmer
#        Chitrajyoti is a Fitness Instructor
#        Srijit is a Coordinator






###############################################################################################################
def funargs7(normal, *argschitrajyoti, **kwargsprogrammer):
    print(normal)
    for item in argschitrajyoti:
        print(item)

    print("\nNow I would like to Introduce sume of our Heroes")

    for key, value in kwargsprogrammer.items():
        # print(key, value)
        print(f"{key} is a {value}")

sourav3 = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Srinjoy", "Spandan", "The Programmer", "Arka", "Subham", "Sukhen"]
normal = "I am a normal Argument and the students are:"
kw = {"Sourav":"Programmer", "Chitrajyoti":"Fitness Instructor", "Srijit":"Coordinator"}
funargs7(normal, *sourav3, **kw)

# output I am a normal Argument and the students are:
#        Sourav
#        Chitrajyoti
#        Srijit
#        Arijit
#        Srinjoy
#        Spandan
#        The Programmer
#        Arka
#        Subham
#        Sukhen
#
#        Now I would like to Introduce sume of our Heroes
#        Sourav is a Programmer
#        Chitrajyoti is a Fitness Instructor
#        Srijit is a Coordinator

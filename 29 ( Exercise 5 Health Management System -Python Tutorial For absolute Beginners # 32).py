# Health Management System
# 3 Clients - Sourav, Chitrjyoti and Srijit
"""
Total 6 files
write a function that when executed takes as input client name
def get.date():
    import datetime
    return datetime.datetime.now()
"""
# one more function  to retrieve exercise of for any client


import datetime
def gettime():
    return datetime.datetime.now()
def take(c):
    if c==1:
        d=int(input("Enter 1 for excersise and 2 for food "))
        if(d==1):
            value=input("Type here\n")
            with open("29 ( Exercise 5 Health Management System(Sourav - ex) -Python Tutorial For absolute Beginners # 32).txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully Written")
        elif(d==2):
            value = input("type here\n")
            with open("29 ( Exercise 5 Health Management System(Sourav - food) -Python Tutorial For absolute Beginners # 32).txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        else:
            print("Please Enter 1 or 2 (Enter 1 for excersise and 2 for food)")
    elif(c==2):
        d = int(input("Enter 1 for excersise and 2 for food "))
        if (d == 1):
            value = input("type here\n")
            with open("29 ( Exercise 5 Health Management System(Chitrajyoti - ex) -Python Tutorial For absolute Beginners # 32).txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        elif (d == 2):
            value = input("Type here\n")
            with open("29 ( Exercise 5 Health Management System(Chitrajyoti - food) -Python Tutorial For absolute Beginners # 32).txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        else:
            print("Please Enter 1 or 2 (Enter 1 for excersise and 2 for food)")
    elif(c==3):
        d = int(input("Enter 1 for excersise and 2 for food "))
        if (d == 1):
            value = input("Type here\n")
            with open("29 ( Exercise 5 Health Management System(Srijit - ex) -Python Tutorial For absolute Beginners # 32).txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        elif (d == 2):
            value = input("Type here\n")
            with open("29 ( Exercise 5 Health Management System(Srijit - food) -Python Tutorial For absolute Beginners # 32).txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        else:
            print("Please Enter 1 or 2 (Enter 1 for excersise and 2 for food)")
    else:
        print("Please enter valid input (1(Sourav),2(Citrajyoti),3(Srijit)")

def retrieve(c):
    if c==1:
        d=int(input("enter 1 for excersise and 2 for food "))
        if(d==1):
            with open("29 ( Exercise 5 Health Management System(Sourav - ex) -Python Tutorial For absolute Beginners # 32).txt") as op:
                for i in op:
                    print(i,end="")
        elif(d==2):
            with open("29 ( Exercise 5 Health Management System(Sourav - food) -Python Tutorial For absolute Beginners # 32).txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Please Enter 1 or 2 (Enter 1 for excersise and 2 for food)")
    elif(c==2):
        d = int(input("Enter 1 for excersise and 2 for food "))
        if (d == 1):
            with open("29 ( Exercise 5 Health Management System(Chitrajyoti - ex) -Python Tutorial For absolute Beginners # 32).txtrohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (d == 2):
            with open("29 ( Exercise 5 Health Management System(Chitrajyoti - food) -Python Tutorial For absolute Beginners # 32).txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Please Enter 1 or 2 (Enter 1 for excersise and 2 for food)")
    elif(c==3):
        d = int(input("Enter 1 for excersise and 2 for food "))
        if (d == 1):
            with open("29 ( Exercise 5 Health Management System(Srijit - ex) -Python Tutorial For absolute Beginners # 32).txt") as op:
                for i in op:
                    print(i, end="")
        elif (d == 2):
            with open("29 ( Exercise 5 Health Management System(Srijit - food) -Python Tutorial For absolute Beginners # 32).txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Please Enter 1 or 2 (Enter 1 for excersise and 2 for food)")
    else:
        print("Please enter valid input (Sourav -> 1,Chitrajyoti -> 2,Srijit ->3 )")


print("Health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for Sourav 2 for Chitrajyoti 3 for Srijit "))
    take(b)
elif a==2:
    c = int(input("Press 1 for Sourav 2 for Chitrajyoti 3 for Srijit "))
    retrieve(c)
else:
    print("Plese ender 1 or 2")

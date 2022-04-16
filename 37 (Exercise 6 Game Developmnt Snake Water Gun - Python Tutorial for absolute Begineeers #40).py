# Snake Water Gun
import random

print("Well Come You to Snake, Water & Gun Game")
print("""*** Rules: 1) You will get 10 Chance to Give Input
2) If You can Enter S for Snake, W for Watter, G for Gun
3) If You Enter S and Computer give input W or If You Enter G and Computer give input S or If You Enter W and Computer give input G for Those Condiction You will be the Winneer
4) Other Wise Computer Will Be Winner
5) After Complete 10 times Input We will declare the Winer
    """)


print("Enter Your Name")
user_name = input()

i = 0
j = 0 # J is for User's score
k = 0 # K is for Computer's score
while(i<10):
    user_input = input("Enter S for Snake, W for Watter, G for Gun ")
    print("You Have Entered", user_input)

    lst = ["S", "W", "G"]
    choice = random.choice(lst)
    print("Output of The Computer is", choice, "\n")

    if user_input == "S" or user_input == "s" and choice == "W":
        i = i + 1
        j = j + 1
    elif user_input == "G" or user_input == "g" and choice == "S":
        i = i + 1
        j = j + 1
    elif user_input == "W" or user_input == "w"and choice == "G":
        i = i + 1
        j = j + 1
    elif user_input == "S" or user_input == "s" and choice == "S":
        i = i + 1
    elif user_input == "W" or user_input == "w" and choice == "W":
        i = i + 1
    elif user_input == "G" or user_input == "g" and choice == "G":
        i = i + 1
    elif choice == "S" and user_input == "W" or user_input == "w":
        i = i + 1
        k = k + 1
    elif choice == "G" and user_input == "S" or user_input == "s":
        i = i + 1
        k = k + 1
    elif choice == "W" and user_input == "G" or user_input == "g":
        i = i + 1
        k = k + 1
    else:
        print("Please enter an Invalid Input. Please Enter S for Snake, W for water & G for Gun")
        i = i + 1

if j > k:
    print("Dear,",user_name, "You Win")
    print("Your Score is", j)
    print("Score of Computer is", k)

elif j == k:
    print("Both of You have Same Same Score. So, any is not Winner")
    print("Your Score is", j)
    print("Score of Computer is", k)

else:
    print("Dear,",user_name, "You are not the winer for this time")
    print("Your Score is", j)
    print("Score of Computer is", k)

# Exercise 3

number_of_guesses=1
print("Number of guesss is limited to only 9 times: ")
while(number_of_guesses<=9):
    guess_number = int(input("\nGuess the number :"))
    if guess_number<18:
        print("You have enter a smaller number please input greater number.")
        print(9 - number_of_guesses,"number of guesses left")
    elif guess_number>18:
        print("You enter a greater number please input smaller number.")
        print(9 - number_of_guesses, "number of guesses left")
    else:
        print("You won")
        print("You won for the",number_of_guesses,"th time of guesses")
        break
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("\nGame over")
import random

# it basically return random number
random_number = random.randint(0, 100)  # random_number = random.randint(0, 100) --> it means it will be return any random number between 0 to 100
print(random_number)



#################################################################################################################
rand = random.random() # it will be generate random number between 0 to 1
print(rand)


# if we want to generate random number between 0 to 100
rand1 = random.random() * 100
print(rand1)


#################################################################################################################
lst = ["Stur Plus", "DD1", "Aaj Tak", "codewithharry"]
choice = random.choice(lst)
print(choice)
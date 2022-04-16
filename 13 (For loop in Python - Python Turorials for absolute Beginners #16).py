list1 = ["Sourav", "Srijit", "Chitrajyoti", "Arijit"]
# print all value of list1 using for loop
for item in list1:
    print(item)    # here the outputs are Sourav
#                                         Srijit
#                                         Chitrajyoti
#                                         Arijit


# print all value of Tuple using for loop
tuple1 = ("Sourav", "Srijit", "Arijit", "Chitrajyoti")
for item in tuple1:
    print(item)    # here the outputs are Sourav
#                                         Srijit
#                                         Arijit
#                                         Chitrajyoti


# print all value value list of list using for loop
list2 = [["Sourav", 1], ["Srijit", 2], ["Chitrajyoti", 3], ["Arijit", 4]]

for item in list2:
    print(item)    # here the outputs are ['Sourav', 1]
#                                         ['Srijit', 2]
#                                         ['Chitrajyoti', 3]
#                                         ['Arijit', 4]


# we can also wright like this
for item, lollypop in list2:
    print(item, lollypop)    # here the outputs are Sourav 1
#                                                   Srijit 2
#                                                   Chitrajyoti 3
#                                                   Arijit 4


# we can also wright like this
for item, lollypop in list2:
    print(item, "and lolly is ", lollypop)    # here the outputs are Sourav and lolly is  1
#                                                   Srijit and lolly is  2
#                                                   Chitrajyoti and lolly is  3
#                                                   Arijit and lolly is  4


# if we want to print list2 just like a dictionary
dict1 = dict(list2)
print(dict1) # here the output is {'Sourav': 1, 'Srijit': 2, 'Chitrajyoti': 3, 'Arijit': 4}



# but we can not wright this line of code
# for item, lollypop in dict1:
#     print(item, "and lolly is ", lollypop)
# if we wright this this type of code we will got error


# but we write code like this
for item, lollypop in dict1.items():
    print(item, "and lolly is ", lollypop) # here the output are Sourav and lolly is  1
#                                                                Srijit and lolly is  2
#                                                                Chitrajyoti and lolly is  3
#                                                                Arijit and lolly is  4


##########################
for item in dict1:
    print(item,) # here the output are Sourav
#                                      Srijit
#                                      Chitrajyoti
#                                      Arijit



# quiz
items = [int, float, "Sourav", 3, 5, 7, 33, 45, 77, 95, 98, 99]

for item in items:
    if  str(item).isnumeric() and item>6:
        print(item) # here the output are 7
#                                         33
#                                         45
#                                         77
#                                         95
#                                         98
#                                         99



####################
items = [int, float, "Sourav", 3, 5, 6, 7, 33, 45, 77, 95, 98, 99]

for item in items:
    if  str(item).isnumeric() and item>=6:
        print(item) # here the output are 6
#                                         7
#                                         33
#                                         45
#                                         77
#                                         95
#                                         98
#                                         99



# if we want to print numbers between 0 to 100
for i in range(0, 100):
    print(i) # here the output are all numbers between 0 - 100
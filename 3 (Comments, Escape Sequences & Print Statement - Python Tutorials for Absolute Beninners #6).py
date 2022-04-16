# Please dont remove this line -> It is called Single line Comments
"""
multi  |
line   |   ---> This is called multi line  Comments
ignore |
now    |
"""

"""This is a comments"""

print("Sourav Ghosh")
print("Electrical Engineer")

# if we want to print multiple line in a Single line then
print("Sourav Ghosh", end="")
print("Electrical Engineer")

# if we want to print both line in same line & want to use ',' after first line then
print("Sourav Ghosh", end=",")
print("Electrical Engineer")

# if we want to print both line in same line & want to provide ' ' then
print("Sourav Ghosh", end=" ")
print("Electrical Engineer")

###########################
print("Sourav Ghosh, Electrical Engineer")

###########################
print("Sourav Ghosh","Electrical Engineer")

###########################
print("Sourav Ghosh","Electrical Engineer")
print("Netaji Subhash Engineering College")

###########################
print("C:\Sourav")

# in case it is C:\nourav then it will be create problem
print("C:\nourav")
"""
Then the output will be C:
                        ourav
"""

# The soluction of this problem is
print("C:\\nourav") # Here we fix this problem by using escape Sequences

# in case we need output like 'C:"Sourav then'
print("C:\"Sourav") # Here we fix this problem by using escape Sequences

# in case we need output like C:'Sourav then
print("C:\'Sourav") # Here we fix this problem by using escape Sequences

############################
print("Sourav is \n a good boy \t 1") # Here we do this by using escape Sequences

#comment after statement
print("Sourav Ghosh is a good boy") # comment after statement

f = open("25 (Writing  and Appending to a file - Python Tutorials for absolute Beginners #28).txt", "w")
f.write("Sourav Bhai bahut achhe hain") # this code can overwrite the original text
# in original text there was Hello World
# now after run this code it will be overwrite by Sourav Bhai bahut achhe hain
f.close()


# if there is not any file with this name then it will be create a file
g = open("25 (Writing  and Appending to a file - Python Tutorials for absolute Beginners(2) #28).txt", "w")
g.write("Sourav Ghosh Bhai bahut achhe hain")
g.close()


# if we run this code then it will be add this line --> Sourav Ghosh ji Bhai bahut achhe hain one after another
h = open("25 (Writing  and Appending to a file - Python Tutorials for absolute Beginners(3) #28).txt", "a")
h.write("Sourav Ghosh ji Bhai bahut achhe hain")
h.close()


# if we want to add this line  --> Sourav Ghosh ji Bhai bahut achhe hain  one after another with a new line then
i = open("25 (Writing  and Appending to a file - Python Tutorials for absolute Beginners(4) #28).txt", "a")
i.write("Sourav Ghosh ji Bhai bahut achhe hain\n")
i.close()


# if we want to know how much char is present
j = open("25 (Writing  and Appending to a file - Python Tutorials for absolute Beginners(5) #28).txt", "a")
a =j.write("Sourav Ghosh ji Bhai bahut achhe hain\n")
print(a)
j.close()


# if want to open a file for read & write then
# handel read & write both
k = open("25 (Writing  and Appending to a file - Python Tutorials for absolute Beginners(6) #28).txt", "r+")
print(k.read()) # here output will be Hello World

k.write("thank you")

k.close()

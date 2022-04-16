d = open("27 (Seek(), tell() & more On Python Files - Python Tutorials For Absolute Beginners #30).txt")
print(d.readline()) # output Sourav Bhai Bahut achhe hain
d.close()


##################################################################
e = open("27 (Seek(), tell() & more On Python Files - Python Tutorials For Absolute Beginners #30).txt")
print(e.readline()) # output Sourav Bhai Bahut achhe hain
print(e.readline()) # output more line
e.close()


##################################################################
f = open("27 (Seek(), tell() & more On Python Files - Python Tutorials For Absolute Beginners #30).txt")
print(f.tell())   # it will be return where is it now(file pointer)  # here output will be 0
print(f.readline()) # output Sourav Bhai Bahut achhe hain
print(f.tell())     # it will be return where is it now(file pointer)  # here output will be 30
print(f.readline())  # output more line
print(f.tell())    # it will be return where is it now(file pointer)  # here output will be 41

f.close()


###########################
g = open("27 (Seek(), tell() & more On Python Files - Python Tutorials For Absolute Beginners #30).txt")
print(g.readline()) # output Sourav Bhai Bahut achhe hain
print(g.seek(0))
print(g.readline()) # output Sourav Bhai Bahut achhe hain  # same line because we use here print(g.seek(0))

g.close()


# if we want to print from 10 char then
print("hhhhh")
h = open("27 (Seek(), tell() & more On Python Files - Python Tutorials For Absolute Beginners #30).txt")
print(h.readline()) # output Sourav Bhai Bahut achhe hain
print(h.seek(7))
print(h.readline()) # output Bhai Bahut achhe hain  # because we use here print(g.seek(7)) so it sart printing from 7 char

h.close()
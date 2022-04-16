# File IO Basic
"""
"r" = Open file for reading  -- default
"w" = Open file for writing
"x" = Create file if not
"a" = Add more file content to a file
"t" = text mode
"b" = binary mode
"+" = read & write
"""

f = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
content = f.read()
print(content) # here output is Sourav is a Good boy
#                               Sourav is  the king of this Universe
#                               Sourav is very smart

f.close()


###########################################################################################################
g = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "r")
content1 = g.read()
print(content1) # here output is Sourav is a Good boy
#                               Sourav is  the king of this Universe
#                               Sourav is very smart

g.close()



# if we do like this then it will be read as binary form
h = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "rb")
content2 = h.read()
print(content2) # here output is b'Sourav is a Good boy\r\nSourav is  the king of this Universe\r\nSourav is very smart'

h.close()


###########################################################################################################
# rt is default mode
i = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "rt")
content3 = i.read()
print(content3) # here output is Sourav is a Good boy
#                               Sourav is  the king of this Universe
#                               Sourav is very smart

i.close()



#############################################################################################################
j = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "rt")
content4 = j.read(3)
print(content4) # here output is Sou

j.close()



###############################################################################################################
k = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "rt")
content5 = k.read(3)
print(content5) # here output is Sou

content5 = k.read(3)
print(content5) # here output is rav


k.close()


###############################################################################################################
l = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "rt")
content6 = l.read(344445)
print(content6)

content6 = l.read(344445)
print(content6)
# here output is Sourav is a Good boy
#                Sourav is  the king of this Universe
#                Sourav is very smart

""" note: here are this type of output because in our text file ---> "23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt"
 we havenot 344445 char so it print compleate txt & print for 1 times"""

l.close()


# another example for perfectly understand
m = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt", "rt")
content7 = m.read(344445)
print("1",content7)

content7 = m.read(344445)
print("2",content7)
# here output is 1 Sourav is a Good boy
#                  Sourav is  the king of this Universe
#                  Sourav is very smart
#                2


""" note: here are this type of output because in our text file ---> "23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt"
 we havenot 344445 char so it print compleate txt & print for 1 times"""

m.close()



############################################################################################################
n = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
content8 = n.read()
for line in content8:
    print(line)

n.close()
# output S
#        o
#        u
#        r
#        a
#        v
#
#        i
#        s
#
#        a
#
#        G
#        o
#        o
#        d
#
#        b
#        o
#        y
#
#
#        S
#        o
#        u
#        r
#        a
#        v
#
#        i
#        s
#
#        t
#        h
#        e
#
#        k
#        i
#        n
#        g
#
#        o
#        f
#
#        t
#        h
#        i
#        s
#
#        U
#        n
#        i
#        v
#        e
#        r
#        s
#        e
#
#
#        S
#        o
#        u
#        r
#        a
#        v
#
#        i
#        s
#
#        v
#        e
#        r
#        y
#
#        s
#        m
#        a
#        r
#        t




# in above condicton it was print char wise if we dont want this type of output then
p = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
content9 = p.read()
for line in p:
    print(line) # here output will be nothing because content9 already read it

p.close()

# slouction of the above problem
q = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
#content10 = q.read()
for line in q:
    print(line)

# here output is Sourav is a Good boy
#
#                Sourav is the king of this Universe
#
#                Sourav is very smart

q.close()


# if we donot need default new line char then
r = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
#content11 = r.read()
for line in r:
    print(line, end="")

# here output is Sourav is a Good boy
#                Sourav is the king of this Universe
#                Sourav is very smart

r.close()


########################################################################################################
print("") # we use this line because we use end="" in above program. # To print output of this program in a line we do this

s = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
print(s.readline())
print(s.readline())
print(s.readline())

# here output is Sourav is a Good boy
#
#                Sourav is the king of this Universe
#
#                Sourav is very smart

s.close()



# if we want to store it in a list then
t = open("23 (Open(), Read & Readline File - Python Tutorial for absolute Beginners #26).txt")
print(t.readlines())  # the output is ['Sourav is a Good boy\n', 'Sourav is the king of this Universe\n', 'Sourav is very smart']


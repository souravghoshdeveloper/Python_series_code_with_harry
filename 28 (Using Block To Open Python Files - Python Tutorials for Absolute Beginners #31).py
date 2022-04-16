t = open("28 (Using Block To Open Python Files - Python Tutorials for Absolute Beginners #31).txt", "rt")
print(t.readlines()) # output ['Sourav Bhai Bahut achhe hain\n', 'more line\n', 'one more line']
print(t.readline())  # this line will be return nothing # Because we already use this line print(t.readlines())

t.close()


#########################################################################
s = open("28 (Using Block To Open Python Files - Python Tutorials for Absolute Beginners #31).txt", "rt")
print(s.readline())   # output Sourav Bhai Bahut achhe hain

s.close()



### with block
with open("28 (Using Block To Open Python Files - Python Tutorials for Absolute Beginners #31).txt") as r:
    a = r.read(4)
    print(a) # # output Sour

# *** Note: in block we dont need to close file

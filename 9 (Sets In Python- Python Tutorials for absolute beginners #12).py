s = set() # it is an empty set
print(type(s)) # Here the output is <class 'set'>

# now we will create a set
# *** here we will create set using list because it it the easiest methode
a_from_list = set([1, 2, 3, 4])
print(a_from_list) # here the output is {1, 2, 3, 4}
print(type(a_from_list)) # Here the output is <class 'set'>


# we can also do this
l = [1, 2, 3, 4]
from_list = set(l)
print(a_from_list) # here the output is {1, 2, 3, 4}
print(type(from_list)) # Here the output is <class 'set'>


s.add(1)
print(s) # here the output is {1}

# in set it does not print same number multiple time
s.add(1)
s.add(1)
print(s) # here the output is {}1 #** here we add 1   2 times but the output is {1} because in set it does not print same number multiple time

# but if we provide multiple number then
s.add(1)
s.add(2)
print(s)  # here the output is {1, 2}

# *** Note: set only retain unique value mens if we give same value multiple time, it will be take it just for one time which is the main difference between list & set



#############################################
s.union({1,2})
print(s)  # Here also the output is {1, 2}

# but if do this then
s1 = s.union({1,2,3})
print(s, s1)  # here the output is {1, 2} {1, 2, 3}


#############################################
s2 = s.intersection({1,2,3})
print(s, s2)  # here the output is {1, 2} {1, 2}


#############################################
print(len(s)) # here the output is 2

print(min(s)) # here the output is 1

print(max(s)) # here the output is 2

print(type(s)) # here the output is <class 'set'>

s3 = {4, 6}
print(s.isdisjoint(s3))  # here the output is True

s3.remove(4)
print(s3) # hee the output is {6}
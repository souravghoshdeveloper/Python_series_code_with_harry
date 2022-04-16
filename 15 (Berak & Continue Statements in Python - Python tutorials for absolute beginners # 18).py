i = 0
while(i<45):
    print(i + 1)
    i = i + 1  # here the output will be 1 - 45


# if we want to print full output in same line then
j = 0
while(j<45):
    print(j + 1) # here the output is 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
    j = j + 1



# but we can't write this type of  code
# m = 0
#while(True):
#    print(m + 1, end=" ")
#    m = m + 1


n = 0
while(True):
    print(n + 1) # here the output will be 1 - 10
    if(n==9):
        break # stop the loop
    n = n + 1


################
p = 0
while(True):
    if p+1<5:
        p = p + 1
        continue
    print(p + 1) # here the output will be 5 - 12
    if(p==11):
        break # stop the loop
    p = p + 1


####################################################################
# break (in break if the condiction is match then the program will be stop at that moment)
k = 0
while(k<10):
    print(k)
    if k == 7:
        break
    k = k + 1 # the output are 1
#                              2
#                              3
#                              4
#                              5
#                              6
#                              7



####################################################################
# continue (in continue if the condiction is match then the program will be skip this part and will be continue after it)
l = 0
while(l<7):
    l = l + 1
    if l == 5:
        continue
    print(l)  # here the output are 1
#                                   2
#                                   3
#                                   4
#                                   6
#                                   7



#################################################3
# Quiz
while(True): # we can write here while(True) or while(1) both are same
    inp = int(input("Enter a number\n"))
    if inp>100:
        print("Congrats you have entered a number greatter than 100\n")
        break
    else:
        print("Try again\n")
        continue
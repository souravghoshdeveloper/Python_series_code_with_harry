import time

# initial2 = time.time()
# print(initial2)


#########################################################################################
initial = time.time()
for i in range(45):
    print("This is Sourav Bhai") # here output is 45 times --> This is Sourav Bhai
print("For loop run in", time.time() - initial, "Seconds")  # This is for basically for show the execution time of this for loop



########################################################################################

print("\n")

initial1 = time.time()
k = 0
while(k<45):
    print("This is Sourav Bhai") # here also output is 45 times --> This is Sourav Bhai
    # k = k + 1
    k +=1
print("While loop run in", time.time() - initial1, "Seconds")   # This is for basically for show the execution time of this while loop

# Note: we can use k = k + 1 or k +=1 both are same




#######################################################################################################################
localtime = time.asctime(time.localtime(time.time()))
print(localtime) # it is basically return localtime




#######################################################################################################################

print("\n")

# If we want to print -->  This is Sourav Ghosh  for 10 times, each after 2 second gap then
i = 0
while(i<10):
    print("This is Sourav Ghosh")
    time.sleep(2)
    i = i + 1
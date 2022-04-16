l1 = ["Bhindi", "Aloo", "chopstick", "chowmein"]

i = 1
for item in l1:
    if i%2!=0:
        print(f"Jarvis Please buy {item}")
    i += 1
# Output Jarvis Please buy Bhindi
#        Jarvis Please buy chopstick




# Enumerate Python
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis Please buy {item}")  # Here output is Jarvis Please buy Bhindi
#                                                            Jarvis Please buy chopstick
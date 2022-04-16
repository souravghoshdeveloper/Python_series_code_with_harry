lis = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Spandan", "Srinjoy", "Arka", "Masud"]

for item in lis:
    print(item, "and", end=" ")

print("other Engineer")
# out of above program --> Sourav and Chitrajyoti and Srijit and Arijit and Spandan and Srinjoy and Arka and Masud and other Engineer


# if we can get same output using join  function
li = ["Sourav", "Chitrajyoti", "Srijit", "Arijit", "Spandan", "Srinjoy", "Arka", "Masud", "Subham"]
a = " and ".join(li)
print(a, "other Electrical Engineer")
# output --> Sourav and Chitrajyoti and Srijit and Arijit and Spandan and Srinjoy and Arka and Masud and Subham other Electrical Engineer

# another example of join function
b = ", ".join(li)
print(b, "other Electrical Engineer")
# output --> Sourav, Chitrajyoti, Srijit, Arijit, Spandan, Srinjoy, Arka, Masud, Subham other Electrical Engineer
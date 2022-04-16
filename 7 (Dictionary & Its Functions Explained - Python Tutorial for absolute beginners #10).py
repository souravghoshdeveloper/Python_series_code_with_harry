# Dictionary & Its Functions -Python Tutorial for absolute beginners #11
# Dictionary is nothing but key value pairs

d1 = {}
print(type(d1)) # output <class 'dict'>

d2 = []
print(type(d2)) # output <class 'list'>

d3 = ()
print(type(d3)) # output <class 'tuple'>



# Dictionary
d4 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti"}
print(d4)  # Here the output is output {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti'}
print((d4["Sourav"])) # output Burger
print((d4["Chitrajyoti"])) # output Fish
print((d4["Arijit"])) # output Roti


d5 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
print(d5["Srinjoy"]) # The output will be {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}
print(d5["Srinjoy"]["B"]) # The output is maggie
print(d5["Srinjoy"]["L"]) # The output is roti
print(d5["Srinjoy"]["D"]) # The output is Chicken


# if we want to add value in dectionary
d6 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d6["Spandan"] = "Junk Food"
print(d6) # the output will be {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Spandan': 'Junk Food'}

# another example
d7 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d7["Spandan"] = "Junk Food"
d7["Arka"] = "Kebabs"
print(d7) # The output will be {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Spandan': 'Junk Food', 'Arka': 'Kebabs'}


# another example
d8 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d8["Spandan"] = "Junk Food"
d8[420] = "Kebabs"
print(d8) # The output will be {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Spandan': 'Junk Food', 420: 'Kebabs'}


# another example
d9 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d9["Spandan"] = "Junk Food"
d9[420] = "Kebabs"
del d9[420]
print(d9) # Here the output will be {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Spandan': 'Junk Food'}

# if we print before del then
d10 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d10["Spandan"] = "Junk Food"
d10[420] = "Kebabs"
print(d10) # Here the output will be {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Spandan': 'Junk Food', 420: 'Kebabs'}
del d10[420]
print(d10) # Here the output will be {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Spandan': 'Junk Food'}



d11 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
print(d11.copy()) # Here also the output is {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}}


d12 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d13 = d12
del d13["Arijit"]  # Here we delete Arijit from d13
print(d12)  # Here the output is {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}}
# Here We delete Arijit from d13 but it is also deleted from d12 because we do here ---> d13 = d12


d14 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d15 = d14.copy()
del d15["Arijit"]
print(d14)  # Here the output is {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}}
# Here we also delete Arijit from d15 but it is not deleted from d14 because we do here ----> d15 = d14.copy()

d16 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
print(d16.get("Sourav")) # Here the output is Burger


########################################
d17 = {"Sourav":"Burger", "Chitrajyoti":"Fish", "Arijit":"Roti", "Srinjoy":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d17.update({"Srijit":"Toffee"})
print(d17) # Here the output is {'Sourav': 'Burger', 'Chitrajyoti': 'Fish', 'Arijit': 'Roti', 'Srinjoy': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Srijit': 'Toffee'}
# We can add data by using d17.update({"Srijit":"Toffee"}) or d17["Srijit"] = "Toffee"


##########################################
print(d17.keys())  # Here the output is dict_keys(['Sourav', 'Chitrajyoti', 'Arijit', 'Srinjoy', 'Srijit'])


##########################################
print(d17.items())  # Here the output is dict_items([('Sourav', 'Burger'), ('Chitrajyoti', 'Fish'), ('Arijit', 'Roti'), ('Srinjoy', {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}), ('Srijit', 'Toffee')])
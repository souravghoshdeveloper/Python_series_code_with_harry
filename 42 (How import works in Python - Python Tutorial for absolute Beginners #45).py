import sklearn as sk
print(sk.__version__) # output 0.23.2. which is the version of sklearn installed in my computer


import sys
print(sys.path)
# output ['E:\\Python\\Python series code with harry', 'E:\\Python\\Python series code with harry', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\win32', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\win32\\lib', 'C:\\Users\\SOURAV\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\Pythonwin']
# according to this output it willbe find sys


#######################################################################################################################
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier)


#######################################################################################################################
import file2  # we import here --> file2.py
file2.a
print(file2.a) # output --> 7 # because in file2.py a=7


#######################################################################################################################
from file2 import a   # we import here --> file2.py
print(a)  # output --> 7
file2.printjoke("This is me")  # Output --> This is a Joke This is me


#######################################################################################################################
# **** Note: PLease dont choose any name for a python file which is a python module
# if you do that you will get an error

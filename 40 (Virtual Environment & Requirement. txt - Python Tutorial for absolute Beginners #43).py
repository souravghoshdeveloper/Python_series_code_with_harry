# This is vast topic
# Please follow 40 (Virtual Environment & Requirement.txt - Python Tutorial For absolute Beginners #44) folder
"""
Procss -- Create Virtual Environment & activate it.
--> python
--> pip
--> pip install virtualenv
--> virtualenv
--> virtualenv souravvirtualenvironment
--> cd souravvirtualenvironment
--> cd Scripts
--> activate

Procss -- if want deactivate Virtual Environment
--> dactivate

# Go instide (after activate) Virtual Environment
--> python
--> import sklearn (if it is installed it on Virtual Environment) ** If it is install on Python Base interpreter but not installed in Virtual Environment
                                                                        then if we run this code on Virtual Environment it will be through an error.

--> pip install sklearn (If we want to install sklearn on Virtual Environment)

--> python
--> import sklearn (if want to know sklearn if Successfully installed or not)
--> exit()


# if want to know which module is installed on your Virtual Environment
--> pip freeze > requrement.txt


# if you want to install spacific version of a module then
--> pip install numpy==1.19.2


# If want to install all module with specific version from requirement.txt
--> pip install -r requrement.txt


######################################################################################################################################
# If you want to create a Virtual Environment with all module which is install on your Base Python Interpreter
--> virtualenv --system-site-packages sarthakvnv
--> cd sarthakvnv
--> cd Scripts
--> activate

--> pip install sklearn (if you run this code. There ootput will be Requirement already satisfied.
                          Because Sklearn is already install on Base Python Interpreter & here We create this Virtual Environment
                          with all module which is install on Base Python Interpreter


--> python
--> import sklearn
--> exit()

--> pip freeze > requrement.txt

--> python
--> import flask (There will be no error because we create this Virtual Environment with all module which is install on Base Python Interpreter
--> exit()
--> deactivate




############################################################################################################################################
# *** Note: If you are not on Virtual Environment then you can create a requirement.txt file for all the information (Which module is installed on Base Python Interpreter
--> pip freeze > requirement.txt


############################################################################################################################################
# *** Note: When you will be run pip freeze > requirement.txt. Please keep on mind the requirement.txt file will be generated on this directory
**** This rule is applicable for Both (Base Python Interpreter & Virtual Environment
"""

print("***Please carefully read this before you enter your name***\n\n""If your name consists of multiple parts, enter them all at once. \nIf it's a single-part name, simply enter that name and then type \"None\" in the next field.\n")

first_name = input("Please enter your Fist Name here")
last_name = input("Please enter your Last Name here")

if (len(first_name or last_name) == 0):
    print("You haven’t entered anything. Please enter your full name.")

elif ((len(first_name)) + (len(last_name)) < 4):
    print("You have entered less than 4 characters. Please make sure that you have entered your First and Last Name.")

elif ((len(first_name)) + (len(last_name)) >25):
    print("You have entered more than 25 characters. Please make sure that you have only entered your First and Last name.")

elif (len(last_name) == 0):
    print("If you do not have a Last Name, please enter \"None\"")

elif (last_name == "None"):
    print("I guess you have no last name.")
    print("Thank you for entering your name.")

else:
    print("Thank you for entering your name.")
#Note for a mentor - I have added an additional variable and few lines to make it bit more complex for me. I hope that is ok 🙂
    



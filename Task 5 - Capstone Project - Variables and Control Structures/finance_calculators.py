import math #To import mathematical fuctions

name = input("Please enter your name: ").capitalize()

print()
#Giving options to choose which calculation user needs
print("🟢 Investment - to calculate the amount of interest you'll earn on your investment")
print("🟢 Bond - to calculate the amount you'll have to pay on a home loan\n")

while True:
    selection = input("👉 Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower()
    if selection != ("investment") and selection != ("bond"):
        print("⚠️  Invalid input. Please enter Investment or Bond only ⚠️")
    else:
        break
#If user select "Investment", the process is as follows
if selection == ("investment"):
    print()
    print("Please answer to the following questions to provide accurate answer\n")

#Questions for user
    initial_deposit = int(input("Please enter the value of your intial deposit: (\u00A3) "))
    interest_rate1 = int(input("Please enter the interest rate (%): "))/100
    years = int(input("Please enter the number of years you are planning to invest: "))
    interest = input("Would you like simple or compound interest? ").lower()

    print()

#Calculations to generate total amount received by the client
    AS = initial_deposit*(1 + interest_rate1*years) #Simple method 
    AC = initial_deposit * math.pow((1+interest_rate1),years) # Compound method

    if interest == ("simple"): #If the client select simple interest method        
        print(f"⭐ \u00A3{AS} is the total amount {name} receive at the end of {years} years under simple interest method""\n")
        print("Thanks for choosing us ❤️")

    elif interest == ("compound"): #If the client select compound interest method        
        print(f"\u00A3{AC} is the total amount {name} receive at the end of {years} years under compound interest method""\n")
        print("Thanks for choosing us ❤️")

    else: #If the client select nothing
        print(f"⭐ \u00A3{AS} is the total amount {name} receive at the end of {years} years under simple interest method")
        print(f"⭐ \u00A3{AC} is the total amount {name} receive at the end of {years} years under compound interest method""\n")
        print("Thanks for choosing us ❤️")

#If user select "Bond", the process is as follows
elif selection == ("bond"):
    print()
    print("Please answer to the following questions to provide accurate answer\n")

#Questions for user
    present_value = float(input("please enter the present value of the house: "))
    interest_rate2 = float (input("Please enter the interest rate (%): "))/100 /12
    months = int(input("Please enter the number of months plan to repay the bond: "))

#Calculation    
    repayment = (interest_rate2 * present_value) / (1 - (1 + interest_rate2)**(-months))

    print("")

    print(f"⭐ \u00A3{repayment} is the total amount {name} has to pay each month for the housing loan\n")

    print("Thanks for choosing us ❤️")

#An error msg for invalid input other than Investment or Bond
else:
    print("❗ERROR - PLEASE ENTER VALID SELECTION (Investment or Bond)")



    







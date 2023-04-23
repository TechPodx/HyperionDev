#Assume -1 means, after antering any negative number program should stop requesting numbers

all_numbers = [] #To save the numbers enter 

number = int(input("Enter a number you like: "))

while number > -1:
    all_numbers.append(number)
    number = int(input("Enter an another number you like: "))
   
else:
    print("")
    averange = sum(all_numbers) / len(all_numbers) #Calculating average of the numbers you entered

    print("The average of the number you entered is: ", averange)
    

    
    

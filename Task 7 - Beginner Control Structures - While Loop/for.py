#**I am creating this file just as additional exercise**
all_numbers = []

number = int(input("Enter a number you like: "))
all_numbers.append(number) #Adding values in "number" to the list

for i in all_numbers:
 
 if i > -1:
   number = int(input("Enter another number you like: "))
   if number > -1: #To avoid negative numbers
    all_numbers.append(number) 
   
   else:
    print("The average of the number you entered is: ", sum(all_numbers) / len(all_numbers)) #Average calculation
    
  

print("****LET'S PLAY A GAME****\n")

equation_file = open("results.txt", "w") #Opening a file to save equations 
 
while True:
  print( )
  start = input("Think two numbers you like & type \"Done\" when you are ready: " ).lower()
  print() #Line space 

  if start == ("done"):
    while True: #Defence
      try:
        number1 = float(input("Enter 1st number you guessed: "))
        break
      except ValueError:
        print("⚠️  Invalid 1st number. Please try again with valid number...🔁\n")
        
    while True: #Defense
      try:
        number2 = float(input("Enter 2nd number you guessed: "))
        break
      except ValueError:
        print("⚠️  Invalid 2nd number. Please try again with valid number...🔁\n")

    while True: #Defense          
      try:
        operation = input("Type the operation (\"+\" , \"-\" , \"*\" , \"/\") you would like: ")
        if operation not in ["+" , "-" , "*" , "/"]:
          raise ValueError("Invalid Operators")
        break
      except ValueError:
        print("⚠️  Invalid operation. Please enter valid operation to process...🔁\n")

#Calculations as per the user selscted operation
    if operation == "+":
      total = number1 + number2
      print( )      
      print(f"{number1} {operation} {number2} = {total}")
      print( )
      with open ("results.txt", "a") as equation_file: #open text file to move input
        equation_file.write(f"{number1} {operation} {number2} = {total}\n") #Write the code into the file.txt
    
    elif operation == "-":
      total = number1 - number2
      print( )
      print(f"{number1} {operation} {number2} = {total}")
      print( )
      with open ("results.txt", "a") as equation_file: #open text file to move input
        equation_file.write(f"{number1} {operation} {number2} = {total}\n") #Write the code into the file.txt
    
    elif operation == "*":
      total = number1 * number2
      print( )
      print(f"{number1} {operation} {number2} = {total}")
      print( )
      with open ("results.txt", "a") as equation_file: #open text file to move input
        equation_file.write(f"{number1} {operation} {number2} = {total}\n") #Write the code into the file.txt
    
    elif operation == "/":
      total = number1 / number2
      print( )
      print(f"{number1} {operation} {number2} = {total}")
      print( )
      with open ("results.txt", "a") as equation_file: #open text file to move input
        equation_file.write(f"{number1} {operation} {number2} = {total}\n") #Write the code into the file.txt

    try_again = input("Do you like to play again (Y/N): ").lower()
    print( )
         
    if try_again == ("y") or try_again == ("yes"):
      print("Please select one of the following options: \n")

      options = input("👉 Please type \"same\" If you want to play same as before using your own numbers\nor\nType \"results\" if you want to print your previous equations with results: ").lower()
      
      if options == ("results"):
        print("Here are your previous results: \n") 
        with open ("results.txt", "r") as file: 
          contents = file.read()
          print(contents) #printing all the data inside of the text file
          print(  )
          print("👇")
          print("Thanks for playing 🙌\n")
          valid_option = True

      else: 
        options == ("same") #if user want to play with their own numbers
        valid_option = False


    else: 
      #try_again != ("y") and try_again != ("yes")
      print("👇")
      print("Thanks for playing 🙌")
      valid_option = True

    if valid_option:
      break

  else:
   print("⚠️  I can not understand what you typed. Please start over 🔁\n") 
  

equation_file.close()


 

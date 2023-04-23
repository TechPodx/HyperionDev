print("I am here to help you for calculating your holiday cost for below destinations\n")

while True:
   cities = ["Paris" , "Toronto", "Madagascar" , "Colombo" , "Tokyo"]
   select_cities = " , ".join(cities) 
   print(select_cities) #Printing a list of cities
   print( )

#Getting input from the user
   while True:
      try:
        city_flight = input("👉 Select one of the above cities you are flying to: ").capitalize()
        if city_flight in cities:
          break
        else:
          print("⚠️  Invalid country name. Please try again with valid input...🔁\n")
      except ValueError:
        print("⚠️  Invalid input. Please try again with valid input...🔁\n")

   while True:
      try:
        num_nights = float(input("👉 Please enter the number of nights you will be staying at a hotel: "))
        break
      except ValueError:
        print(("⚠️  Invalid input. Please try again with a valid number...🔁\n"))
 
   while True:
     try:
        rental_days = float(input("👉 Please enter the number of days that you will be hiring a car for: "))
        break
     except ValueError:
        print(("⚠️  Invalid input. Please try again with a valid number...🔁\n"))
  
   print( )
#Define a fuctions
   def hotel_cost(num_nights , hotel_charge):
     total1 = num_nights * hotel_charge
     return total1
    
   def plane_cost(plane_charge):
     total2 = plane_charge
     return total2

   def car_rental(rental_days , car_charge):
     total3 = rental_days * car_charge
     return total3

   def holiday_cost(hotel , plane , car):
     total_budget = (hotel + plane + car)
     return total_budget

#Calculate based on the city the user select
   if city_flight == ("Paris"):
     hotel = hotel_cost(num_nights , (50))
     plane = plane_cost(220)
     car = car_rental(rental_days , (40))
     print( )
     print("Your total holiday  cost is:\u00A3" , holiday_cost(hotel , plane , car) )
     print( )

   elif city_flight == ("Toronto"):
     hotel = hotel_cost(num_nights , (45))
     plane = plane_cost(250)
     car = car_rental(rental_days , (35))
     print( )
     print("Your total holiday  cost is:\u00A3" , holiday_cost(hotel , plane , car))
     print( )

   elif city_flight == ("Madagascar"):
     hotel = hotel_cost(num_nights , (30))
     plane = plane_cost(210)
     car = car_rental(rental_days , (20))
     print( )
     print("Your total holiday  cost is:\u00A3" , holiday_cost(hotel , plane , car))
     print( )

   elif city_flight == ("Colombo"):
     hotel = hotel_cost(num_nights , (31))
     plane = plane_cost(290)
     car = car_rental(rental_days , (18))
     print( )
     print("Your total holiday  cost is:\u00A3" , holiday_cost(hotel , plane , car))
     print( )

   elif city_flight == ("Tokyo"):
     hotel = hotel_cost(num_nights , (39))
     plane = plane_cost(248)
     car = car_rental(rental_days , (22))
     print( )
     print("Your total holiday  cost is: \u00A3", holiday_cost(hotel , plane , car))
     print( )

   else:
     print("Unrecognized options ⚠️. Please try again!\n")

   
   try_again = input("Do you want to find cost for an another holiday destination?: ").lower()
   print()
   if try_again == ("yes") or try_again == ("y"):
      continue
      
   
   elif try_again == ("no") or try_again == ("n"):
      print("Thanks for using us. Enjoy your journey ❤️")
      break
   
   else:
     print("⚠️  Invalid input. Try again")
     print()
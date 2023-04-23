menu = ["Burger" , "Chicken Wrap" , "Pizza" , "Donut"]

print()

stock = {
        "Burger" : int(input("Qty of Burgers: "))
       ,"Chicken Wrap" : int(input("Qty of Chicken Wraps: "))
      , "Pizza" : int(input("Qty of Pizzas: "))
      , "Donut" : int(input("Qty of Burgers: "))
        }

print() 

price = {
        "Burger" : int(input("Price of a Burger: "))
        ,"Chicken Wrap" : int(input("Price of a Chicken Wrap: ")), 
        "Pizza" : int(input("Price of a Pizza: ")), 
        "Donut" : int(input("Price of a Donut: "))
        }

print()

print("Total worth of the currect stock as per below: \n")

total_burger = (stock["Burger"] * price["Burger"])
total_wrap = (stock["Chicken Wrap"] * price["Chicken Wrap"])
total_pizza = (stock["Pizza"] * price["Pizza"])
total_donut = (stock["Donut"] * price["Donut"])

print()

print("Total stock value of Burger: " , total_burger)
print("Total stock value of Chicken Wrap: " , total_wrap)
print("Total stock value of Pizza: " , total_pizza)
print("Total stock value of Donut: " , total_donut)

print()

print("The total stock value at the cafe is: " , (total_burger + total_wrap + total_pizza + total_donut))

print()
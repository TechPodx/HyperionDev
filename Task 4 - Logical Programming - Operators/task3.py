#Calculating total time for the events 
swimming = input("Swimming - Enter your finishing time")
cycling = input("Cycling - Enter your finishing time")
running = input("Running - Enter your finishing time")

total_time = int(swimming) + int(cycling) + int(running)
print("Your total finishing time = ",int(total_time))

if total_time <= int(100):
    print("You have been awarded Provincial Colours 🥇💐")

elif total_time > int(100) and total_time <= int(105):
    print("You have been awarded Provincial Half Colours 🥈💐 ")

elif total_time > int(105) and total_time <= int(110):
    print("You have been awarded Provincial Scroll 🥉💐")

else:
    print("You have not been received any award this time 💔\n Not receiving an award can be disappointing, but it's important to remember that it doesn't define your worth or capabilities. \n So, keep pushing yourself, stay focused on your goals, and believe in your ability to achieve them. The next time may be your moment to shine!⭐")

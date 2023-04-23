#Getting input from user to design the grid
sample_grid = []
design_grid = []

while True:  
    try:
#Defensing invalid user input     
      num_rows = int(input("Eneter a number between 3 to 10 to create rows: "))
      if num_rows <= 10 and num_rows >=3: #Checking the range of user input
         break
      
      else:
         print("⚠️  Invalid input. Please enter a number between 3 to 10 ⚠️")

    except ValueError:
       print("⚠️  Invalid input. Please use numbers only ⚠️")
#Defensing invalid user input     
while True:
    try:
      num_columns = int(input("Eneter a number between 3 to 10 to create columns: "))
      if num_columns <= 10 and num_columns >= 3: #Checking the range of user input
         break

      else:
         print("⚠️  Invalid input. Please enter a number between 3 to 10 ⚠️")

    except ValueError:
       print("⚠️  Invalid input. Please enter numbers only ⚠️")

print()
print("This is the sample size of your grid based on your input\n")

for x in range(num_rows):
    row = []
    for y in range(num_columns):
        row.append(f"({x},{y})")
    sample_grid.append(row)
    print(row)
    print()

print()
print("Instructions 👉 If you want to mark a spot on the grid as a mine 💣, enter the hash symbol \"#\" or enter dash symbol \"-\" to represent a spot that is free of mines 🌻.\n")

#Getting input to design actual grid
times = (num_rows * num_columns) #Total number of symbols
for x in range(num_rows):
    row = []
    for y in range(num_columns):
        while True:
           try:
              design_input = input(f"Now it is time to place your symbols (# or -) into row {x} and column {y} to design your grid: ")
              if design_input != ("#") and design_input != ("-"):
                print("⚠️  Invalid input. Please use only \"#\" or \"-\" ⚠️")
              else:
                break
           except ValueError:
              print("Please follow the given instructions")
        times -= 1 #Number of time left to enter
            
        if times > 0: #To avoid printing "you still have 0 times out of..." statement
           print(f"👉 You still have (🔸{times}🔸) times out of {num_rows * num_columns} times to go. Keep going 👏")

        row.append(design_input)
    design_grid.append(row)
print()
print("✳️  The grid after placing your input ✳️")
print()
for row in design_grid:
    print(row)

print()
print("👉 Below grid shows where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot.\ni.e. (horizontally, vertically, and diagonally)\n")
print("✳️  Final Output ✳️\n")

def find_mines(design_grid):
   final_grid = []
   for x in range(num_rows):
      row = []
      for y in range(num_columns):
         if design_grid [x][y] == "#":
            row.append("[💥]")
         else:
            number = 0
            #Counting number of bombs
            for xx in range(max(0 , x-1) , min(num_rows , x+2 )):
               for yy in range(max(0 , y-1) , min(num_columns , y+2)):
                    if design_grid[xx][yy] == "#":
                        number += 1
            row.append(str([number])) #Adding number of bombs to the rows
      final_grid.append(row)
   return final_grid

final_output = find_mines(design_grid)
for row in final_output: #To print as rows
    print(row)
        
print()
print("Hope you enjoy the game 😍. Thanks for your time 🙂")
while True:
   star = "*"
   print(star * 50)
   break

print()
print("Thanks for checking my answer 🙏🙂 and Highly appreciate all of your effort to make this success 💖")
print()
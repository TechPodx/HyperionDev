# *1st Question

story1 = "\"The!quick!brown!fox!jumps!over!the!lazy!dog!.\""
story1_0 = story1.replace("!", " ") #This removes "!" and replace with " "
story1_1 = (story1_0.replace("dog ." , "dog.")) #This removes the small space between "dog" and "."

print(story1_1)
#The reason I added addiotional lines is to generate the exact output given in the question pdf

# *2nd Question

story_upper = (story1_1.upper())

print(story_upper) #Turn all letters to upper letters

# *3rd Question (Assumtion - using 2nd question output to the 3rd question)

stroy_upper_reverse = story_upper[ ::-1]
print(stroy_upper_reverse)

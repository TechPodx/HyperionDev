word = "Hyperiondev is the best bootcamp in the UK\n"

new_word1 = "" #To save upper and lower letters of 1st question
new_word2 = "" #To save lower and upper letters of 2st question

for i in range(len(word)):
    if i % 2 == 0: #Condition
        new_word1 += word[i].upper()
        new_word2 += word[i].lower()
        

    else:
        new_word1 += word[i].lower()
        new_word2 += word[i].upper()

print()
print(f"Answer for the 1st question:  {new_word1}")
print()
print(f"Answer for the 2nd question:  {new_word2}")


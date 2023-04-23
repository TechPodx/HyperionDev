import spacy
nlp = spacy.load("en_core_web_md")

tokens = nlp("cat apple monkey banana ")
for token1 in tokens:
  for token2 in tokens:
    print(token1.text, token2.text, token1.similarity(token2))

'''
******similarities between cat, monkey and banana*******

--Out put--

cat cat 1.0
cat apple 0.20368057489395142
cat monkey 0.5929929614067078
cat banana 0.2235882729291916
apple cat 0.20368057489395142
apple apple 1.0
apple monkey 0.2342509627342224
apple banana 0.6646700501441956
monkey cat 0.5929929614067078
monkey apple 0.2342509627342224
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882729291916
banana apple 0.6646700501441956
banana monkey 0.4041501581668854
banana banana 1.0

According to the output, we can observe below similarities

   - When the for loop iterates over "cat" and "monkey," the resulting similarity rate is 0.59299..., whereas when it compares "cat" to "apple," the similarity rate is lower at 0.20368...
   - The reason for the discrepancy in similarity rates between "cat" and "monkey" (0.59299...) and "cat" and "apple" (0.20368...) when the for loop is applied is due to the fact that spaCy recognizes "cat" and "monkey" as both being animals, while "cat" and "apple" are recognized as an animal and a fruit, respectively.
   - Similarly to the previous comparison, the similarity rate between "apple" and "banana" is higher at 0.664670... because spaCy recognizes both as fruits.
   - Based on the above results, the noteworthy observation is that the relationship rate between "monkey" and "banana" is as high as 0.404150, despite the objects being different. This demonstrates the model's ability to recognize practical real-world relationships between objects. However, we cannot observe a similar relationship between "cat" and "banana," or "cat" and "apple."
'''

print()
print("****Comparison on my own example****")

tech = ["Computer" , "Processor" , "Car" , "AI" , "Chicken"]

# Creating list of token for each item
tech_token = [nlp(name) for name in tech]

# create a loop to compare the similarities
for i, token1 in enumerate(tech_token):
  print()
  for j, token2 in enumerate(tech_token):
    if i != j:
      similarity = token1.similarity(token2)
      print(f"{tech[i]} - {tech[j]}: {similarity}")

'''
*****Answer - Note on my own example *****

- It is evident that the relationship indicators for the following tokens are higher compared to the others.
       Computer - Processor: 0.5098316187381035
       Computer - AI: 0.4365837847139069
       Processor - AI: 0.30764577437205076

- Meanwhile, the other tokens are demonstrating very low relationships between them.
       AI - Chicken: -0.0027645890789996875
       Computer - Chicken: 0.002910880848102762
       Car - AI: 0.08868873477128354
       Car - Chicken: 0.14055677611502232
       Processor - Car: 0.17778584198435549
       Processor - Chicken: 0.12759245657082693
       Car - Computer: 0.24828874640751364

'''
print()
print("👉 Answer to the question number three is attached in seperate Excel file. Please check that")
print()

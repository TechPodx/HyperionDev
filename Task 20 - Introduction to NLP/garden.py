import spacy
nlp = spacy.load("en_core_web_sm")

#Adding 3 garden path sentences to a list
gardenpathSentences = [
                       "The chicken is ready to eat fried." ,
                       "The horse raced past the barn fell." ,
                       "The old man the boat." ,
                      ]

#Adding another 3 as suggested
gardenpathSentences.extend([
                            "Mary gave the child a Band-Aid." , 
                            "That Jill is never here hurts." ,
                            "The cotton clothing is made of grows in Mississippi."
                          ])

# You will get the full list of GP sentences
print("🟢 This is the full list of Gargen Path Sentences")
print()
print(gardenpathSentences)

# Tokenizing sentences
print()
print("🟢 Results after tokenizing each sentence")
print()
for sentences in gardenpathSentences:
    doc_nlp = nlp(sentences)
    for token in doc_nlp:
        print(token.text) 

# Performing Named Entity Recognition
print()
print("🟢 Results of Named Entity Recognition")
print()
for sentences in gardenpathSentences:
    doc_nlp = nlp(sentences)
    for ent in doc_nlp.ents:
        print(ent.text ,"-", ent.label_)
        print("👉 Meaning of entity named " , ent.label_ , " is " , spacy.explain(ent.label_))
        print()

# ***** Comments about two entities *****

# PERSON - People, including fictional
# This entity refers to individuals or group of people, such as names of persons, family names or group names. 
# I do have a sense in terms of "Mary" recognised as a PERSON entity.

# GPE - Countries, cities, states
# This refers to geopolitical entities, such as countries, cities, states, or provinces
# This makes sense as it recognised Mississippi as a GPE entity as it is a state





    
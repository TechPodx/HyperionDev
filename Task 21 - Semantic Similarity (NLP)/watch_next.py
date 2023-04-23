import spacy
nlp = spacy.load("en_core_web_md")

def best_movie(description):
  with open("movies.txt" , "r") as txtfile: # To open txt file
    movies_list = txtfile.readlines() #

  # Assigning variables to store data
  highest_similarity = 0
  most_suitable_movie = " "
    
  for movie in (movies_list):
    movie = movie.strip()
    sim_check = (nlp(description).similarity(nlp(movie)))
    # Setting conditions to get stored the highest values and the relavent movie
    if sim_check > highest_similarity:
      highest_similarity = sim_check
      most_suitable_movie = movie[0:8]
  
  return most_suitable_movie

print()
ask = input("Do you want a recommondation to watch your next movie (Yes/No) 😍: ").lower()
print()

if ask == ("yes") or ask == ("y"):
  # Set the job description that we want to compare
  description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
  the_best = best_movie(description)
  print("⭕ You will propably like: " , the_best ,"✳️ ", "I hope you love it👌")
  print()

else:
  print("🔸Thanks for using us 💚")
  print()


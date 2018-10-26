pets = ('cat', 'cat', 'cat', 'dog', 'horse')
c = pets.count("cat")
d = len(pets)
if (c/d)*100 > 50.0:
  print("There are too many cats here")
else:
  print("Everything is good")
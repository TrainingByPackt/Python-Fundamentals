sentence = input("Sentence: ")
query = input("Word to look for in sentence: ")

# sanitize our inputs
sentence = sentence.lower().strip()
query = query.lower().strip()

num_occurrences = sentence.count(query)

print(f"There are {num_occurrences} occurrences of '{query}' in the sentence.")

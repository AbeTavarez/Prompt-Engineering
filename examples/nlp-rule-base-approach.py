# Sample rule-based approach for POS tagging

# Define some word lists based on categories
nouns = ["dog", "cat", "man", "woman", "ball", "sky"]
verbs = ["run", "eat", "play", "see", "bark"]
adjectives = ["blue", "fast", "tall", "bright"]
articles = ["the", "a", "an"]

# Function to assign a POS tag based on basic rules
def pos_tagger(sentence):
    # Tokenize the sentence into words
    words = sentence.lower().split()
    
    # Initialize an empty list to store word-POS pairs
    tagged_sentence = []
    
    for word in words:
        # Check for different parts of speech based on simple rules
        if word in nouns:
            tagged_sentence.append((word, "NOUN"))
        elif word in verbs:
            tagged_sentence.append((word, "VERB"))
        elif word in adjectives:
            tagged_sentence.append((word, "ADJ"))
        elif word in articles:
            tagged_sentence.append((word, "ART"))
        else:
            tagged_sentence.append((word, "UNKNOWN"))  # For words not in our lists
    
    return tagged_sentence

# Example sentence
sentence = "The dog runs fast and sees the blue ball"

# Apply the POS tagger
tagged_output = pos_tagger(sentence)

# Print the tagged sentence
for word, tag in tagged_output:
    print(f"{word}: {tag}")

import nltk
from nltk.stem import PorterStemmer

nltk_version = nltk.__version__

print('NLTK Library imported, version: ', nltk_version)

# Sample email content for stemming
email_content = "Our team will be working on the upcoming project deadlines. Please ensure that all deliverables are submitted before the end of the week."

# Create a Porter Stemmer instance
porter_stemmer = PorterStemmer()

# Apply stemming to each word in the email content
stemmed_words = [porter_stemmer.stem(word) for word in nltk.word_tokenize(email_content)]

print(stemmed_words)
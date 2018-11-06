# Import the NLTK Library and Wordnet corpus
import nltk
from nltk.corpus import wordnet as wn


# Function to get synonyms of the entered word
def get_synonyms(word):

    # Declare an empty list to store all the synonyms
    synonyms = []

    # Wordnet groups words as sets of synonyms called "synsets".
    # Iterate over the synsets of the word to extract all synonyms
    for synset in wn.synsets(word):

        # Update the list of synonyms
        synonyms.extend(synonym for synonym in synset.lemma_names() if synonym not in synonyms)
    return synonyms

# Execute the script
if __name__ == '__main__':
    
    # Get the word from the user
    word = input('Type in the word and press ENTER\n')
    print(get_synonyms(word))

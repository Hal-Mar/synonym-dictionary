# Import the NLTK Library and Wordnet corpus
import nltk
from nltk.corpus import wordnet as wn


# Function to get synonyms of the entered word given the POS
def get_synonyms(word, pos):

    # Declare empty lists to store all the synonyms and the result
    synonyms = []
    result = []
    # Wordnet groups words as sets of synonyms called "synsets".
    # Iterate over the synsets of the word to extract all synonyms
    for synset in wn.synsets(word, pos=pos):
        # Update the list of synonyms
        synonyms.extend(synonym for synonym in synset.lemmas() if synonym not in synonyms)
    
    # Return empty list if no synonyms
    if len(synonyms) <= 0:
        return []
    
    # The first lemma in the list of synonyms is the "synset" object of input word
    input_word = synonyms[0]

    # Iterate over the list of synonyms to get synonyms and their similarity with entered word
    for s in synonyms:
        result.append((s.name(), input_word.synset().wup_similarity(s.synset())))

    # Return the result
    return result

# Execute the script
if __name__ == '__main__':
    
    # Get the word from the user
    word = input('Type in the word and press ENTER\n')
    pos = input('Enter the part of speech (N=noun, V=verb, J=adjective, R=adverb)\n')

    if pos == 'N' or pos == 'n':
        pos = wn.VERB
    elif pos == 'V' or pos == 'v':
        pos = wn.NOUN
    elif pos == 'J' or pos == 'j':
        pos = wn.ADJ
    elif pos == 'R' or pos == 'r':
        pos = wn.ADV
    
    print(get_synonyms(word, pos))

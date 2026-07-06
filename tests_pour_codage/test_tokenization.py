import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

texte = "Bonjour! www.francetv.fr 345555 Comment ça va aujourd'hui? Lucas.Inc 32"
liste_tokens = word_tokenize(texte)
print(liste_tokens)

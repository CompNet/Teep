#importations
from nltk.stem import SnowballStemmer

# on choisit le langage à partir duquel on veut raciniser:
stemmer = SnowballStemmer("english")

#on peut alors raciniser un mot. 
a = stemmer.stem("publisher")
print(a)

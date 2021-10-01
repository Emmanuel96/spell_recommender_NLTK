import nltk as nltk
from nltk.corpus import words
nltk.download('words')

correct_spellings = nltk.corpus.words.words()
# stop_words = set(stopwords.words('english'))

from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

import warnings

warnings.filterwarnings('ignore')

def recommender_with_jaccard_distance_answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
     
    for entry in entries:
        temp = [(jaccard_distance(set(ngrams(entry, 3)), set(ngrams(w, 3))),w) for w in correct_spellings if w[0]==entry[0]]
        print(sorted(temp, key = lambda val:val[0])[0][1])
    return # Your answer here
    

from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

import warnings

warnings.filterwarnings('ignore')

def recommender_with_jaccard_distance(entries=['cormulent', 'incendenece', 'validrate']):
     
    for entry in entries:
        temp = [(jaccard_distance(set(ngrams(entry, 4)), set(ngrams(w, 4))),w) for w in correct_spellings if w[0]==entry[0]]
        print(sorted(temp, key = lambda val:val[0])[0][1])
    return # Your answer here
    

from nltk.metrics.distance  import edit_distance

def spell_recommender_with_editdistance(entries=['cormulent', 'incendenece', 'validrate']):
    for entry in entries:
        temp = [(edit_distance(entry, w),w) for w in correct_spellings if w[0]==entry[0]]
        print(sorted(temp, key = lambda val:val[0])[0][1])
    return

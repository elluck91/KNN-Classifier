import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords
import pandas as pd
import re

def clear_review(text):
    '''
    Utility method cleaning the reviews. It uses NLTK library and PorterStemmer to remove
    ends of words that have the same basis, such as "grow" and "grows."
    
    Also, it remove stop words, such as "a", "an", etc.
    '''

    # remove NON_ASCII characters
    temp1 = re.sub(r'\W+',' ', text)
    # word tokenize
    tempSentenceArray = nltk.word_tokenize(temp1)

    temp2 = []
    
    # SnowballStemmer and lowercase and length of 4, which includes stopwords
    ps = PorterStemmer()
    for word in tempSentenceArray:
        if len(word) >= 4:
            temp2.append(ps.stem(word))
        
    return temp2

def processFile(path):
    df = pd.read_csv(
        filepath_or_buffer=path, 
        header=None, 
        sep='\n')


    # separate names from classes
    vals = df.iloc[:,:].values
    reviews = [n[0][3:] for n in vals]
    cls = [n[0][0] for n in vals]
    
    revs = []
    
    for t in range(0, len(reviews)):
        revs.append(clear_review(reviews[t]))

    file = open("tokenized_reviews.dat","w")
    for i in range(0, len(revs)):
        file.write(cls[i] + ",")
        for word in revs[i]:
            file.write(word + ",")
            
        file.write("\n")
    
    file.close()
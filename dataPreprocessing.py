import nltk
from nltk.stem.porter import *
import pandas as pd
import re
from collections import defaultdict, Counter
import pickle
import numpy as np
from scipy.sparse import csr_matrix

#==============================================================================
# PREPROCESSING
# 
# 1. READ IN THE TEXT DATA
# 2. REMOVE ALL NON-ASCII CHARACTERS
# 3. TOKENIZE WORDS
# 4. STEM THE WORDS AND TURN TO LOWERCASE
# 5. SAVE IT TO A FILE
#==============================================================================


def clear_review(text):
    '''
    Utility method cleaning the reviews. It uses NLTK library and PorterStemmer to remove
    ends of words that have the same basis, such as "grow" and "grows."
    
    Also, it remove stop words, such as "a", "an", etc.
    '''
    print text
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

def processLabeledFile(path, name):
    path = path + ".dat"
    df = pd.read_csv(
        filepath_or_buffer = path, 
        header=None, 
        sep='\n')


    # separate names from classes
    vals = df.iloc[:,:].values
    reviews = [n[0][3:] for n in vals]
    cls = [n[0][0] for n in vals]
    
    revs = []
    
    for t in range(0, len(reviews)):
        revs.append(clear_review(reviews[t]))

    file = open(name + ".dat","w")
    for i in range(0, len(revs)):
        file.write(cls[i] + ",")
        for word in revs[i]:
            file.write(word + ",")
            
        file.write("\n")
    
    file.close()
    
    return revs

def processFile(path, name):
    path = path + ".dat"
    df = pd.read_csv(
        filepath_or_buffer = path, 
        header=None, 
        sep='\n')

    vals = df.iloc[:,:].values
    reviews = [n[0][:] for n in vals]
    
    revs = []
    for t in range(0, len(reviews)):
        revs.append(clear_review(reviews[t]))

    file = open(name + ".dat","w")
    for i in range(0, len(revs)):
        for word in revs[i]:
            file.write(word + ",")
        file.write("\n")
    file.close()
    
    return revs
    
def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
def buildDictionary():
    df = pd.read_csv(
        filepath_or_buffer='tokenized_reviews.dat', 
        header=None, 
        sep='\n')
    
    vals = df.iloc[:,:].values
    reviews = [n[0][2:].split(',') for n in vals]
    
    index = defaultdict(list)
    for i in range(0, len(reviews)):
        for word in reviews[i]:
            if i not in index[word]:
                index[word].append(i)
        
#save_obj(index, "dictionary")
    
#    read = load_obj("dictionary")

def build_inverted_index(reviews):
    index = defaultdict(list)
    for i in range(0, len(reviews)):
        l2norm = np.sqrt(len(reviews[i]))
        val = 1/l2norm
        for word in reviews[i]:
            print "Review #" + str(i) + ":"
            if word not in index:
                index[word].append((i, val))
            elif (i, val) not in index[word]:
                print "adding " + str(i) + " to II"
                index[word].append((i, val))
                
    return index









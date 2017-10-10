from nltk.classify import NaiveBayesClassifier
import pandas as pd
import re
 
def word_feats(words):
    return dict([(word, True) for word in words])

# return [ [t for t in d if len(t) >= minlen ] for d in docs ] 
def filterLen(doc, minlen):
    arr = []
    for t in doc:
        if len(t) >= minlen:
            arr.append(t)
    return arr
    

def clean_tweet(text):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

df = pd.read_csv(
    filepath_or_buffer='train.dat', 
    header=None, 
    sep='\n')


# separate names from classes
vals = df.iloc[:,:].values
reviews = [n[0][3:] for n in vals]
cls = [n[0][0] for n in vals]

revs = []
for t in range(0, len(reviews)):
    revs.append(clean_tweet(reviews[t]))

completeReviews = []

for t in range(0, len(revs)):
    completeReviews.append(filterLen(revs[t].split(" "), 4))
        
negfeats = []
posfeats = []
for i in range(0, len(completeReviews)):
    if cls[i] == "-":
        word = (word_feats(completeReviews[i]), 'neg')
        negfeats.append(word)
    elif cls[i] == "+":
        word = (word_feats(completeReviews[i]), 'pos')
        posfeats.append(word)
 
trainfeats = negfeats + posfeats

df = pd.read_csv(
    filepath_or_buffer='test.dat', 
    header=None, 
    sep='\n')


# separate names from classes
vals = df.iloc[:,:].values
reviews = [n[0][:] for n in vals]

revs = []
for t in range(0, len(reviews)):
    revs.append(clean_tweet(reviews[t]))

completeReviews = []

for t in range(0, len(revs)):
    completeReviews.append(filterLen(revs[t].split(" "), 4))

testfeats = [];

for i in range(0, len(completeReviews)):
    testfeats.append(word_feats(completeReviews[i]))
    

print "Length of testfeats: " + str(len(testfeats))
classifier = NaiveBayesClassifier.train(trainfeats)
#classifier.classify_many(testfeats)

file = open("test.dat","w")

for pdist in classifier.prob_classify_many(testfeats):
    if pdist.prob('neg') > pdist.prob('pos'):
        file.write("-1\n")
    else:
        file.write("+1\n")
file.close()
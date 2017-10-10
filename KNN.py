import pandas as pd
from dataPreprocessing import processFile

#=========================== MAIN =============================================


#==============================================================================
# PREPROCESSING
# 1. TURN ALL TEXT TO LOWERCASE
# 2. REMOVE HTML
# 3. STEMMING
# 4. REMOVE STOPWORDS
#==============================================================================
processFile("train.dat")

df = pd.read_csv(
        filepath_or_buffer='tokenized_reviews.dat', 
        header=None, 
        sep='\n')

#==============================================================================
# completeReviews = []
# 
# for t in range(0, len(revs)):
#     completeReviews.append(filterLen(revs[t].split(" "), 4))
#         
# negfeats = []
# posfeats = []
# for i in range(0, len(completeReviews)):
#     if cls[i] == "-":
#         word = (word_feats(completeReviews[i]), 'neg')
#         negfeats.append(word)
#     elif cls[i] == "+":
#         word = (word_feats(completeReviews[i]), 'pos')
#         posfeats.append(word)
#  
# trainfeats = negfeats + posfeats
# 
# df = pd.read_csv(
#     filepath_or_buffer='test.dat', 
#     header=None, 
#     sep='\n')
# 
# 
# # separate names from classes
# vals = df.iloc[:,:].values
# reviews = [n[0][:] for n in vals]
# 
# revs = []
# for t in range(0, len(reviews)):
#     revs.append(clean_tweet(reviews[t]))
# 
# completeReviews = []
# 
# for t in range(0, len(revs)):
#     completeReviews.append(filterLen(revs[t].split(" "), 4))
# 
# testfeats = [];
# 
# for i in range(0, len(completeReviews)):
#     testfeats.append(word_feats(completeReviews[i]))
#     
# 
# print "Length of testfeats: " + str(len(testfeats))
# classifier = NaiveBayesClassifier.train(trainfeats)
# #classifier.classify_many(testfeats)
# 
# file = open("test.dat","w")
# 
# for pdist in classifier.prob_classify_many(testfeats):
#     if pdist.prob('neg') > pdist.prob('pos'):
#         file.write("-1\n")
#     else:
#         file.write("+1\n")
# file.close()# -*- coding: utf-8 -*-
# 
# 
#==============================================================================

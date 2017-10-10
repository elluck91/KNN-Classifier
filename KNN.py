import pandas as pd
import numpy as np
from dataPreprocessing import load_obj, build_inverted_index, save_obj, processFile, clear_review
from collections import Counter

#============ READ TOKENIZED TRAINING DATASET =================================
df = pd.read_csv(
    filepath_or_buffer='tokenized_reviews.dat', 
    header=None, 
    sep='\n')

# separate names from classes
vals = df.iloc[:,:].values
reviews = [n[0][2:].split(',') for n in vals]
classes = [n[0][:1] for n in vals]


#================= INVERTED INDX ALREADY CREATED ==============================
#inverted_index = build_inverted_index(reviews)
#save_obj(inverted_index, "inverted_idx")


#================= LOAD INVERTED IDX FOR COMPUTING TESTSET ====================
inverted_idx = load_obj("inverted_idx")
#================ PROCESS AND TOKENIZE TESTSET FOR FUTURE USE =================
#querries = processFile("fake_test", "tokenized_test")
df = pd.read_csv(
    filepath_or_buffer='train.dat', 
    header=None, 
    sep='\n')

# separate names from classes
values = df.iloc[:1000,:].values
querries = [n[0][2:] for n in values]
querryClasses = [int(n[0][:2]) for n in values]


#================== COMPUTE ACCUMULATOR FOR EACH QUERRY========================
s = (len(querries), len(vals))
querry_accumulator = np.zeros(s)

review_id = 0
for querry in querries:
    review = clear_review(querry)
    val = 1/np.sqrt(len(review))
    
    word_count = 1;
    for word in review:
        for doc in inverted_idx[word]:
            querry_accumulator[review_id][doc[0]] += val * doc[1]
        word_count += 1
    review_id += 1
#======= SELECT K NEAREST NEIGHBORS AND PICK CLASS USING MAJORITY =============
K = 10
querry_classes = np.zeros(len(querries))
best = (None, None)
for k in range(1, K):
    acc = 0.0
    temp_classes = np.zeros(k)

    for i in range(0, len(querries)):
        temp = querry_accumulator[i].argsort()[-k:][::-1]
        for cl in range(k):
            if classes[temp[cl]] == "+":
                cla = "+1"
            else:
                cla = "-1"
            temp_classes[cl] = cla
        c = Counter(temp_classes);
        val, blah = c.most_common()[0]
        querry_classes[i] = int(val)
        
    for i in range(len(querry_classes)):
        if querry_classes[i] == querryClasses[i]:
            acc += 1
    print str(acc/len(querry_classes))
        
    
        
#=================== check accuracy on fake_test.dat ==========================


#============ WRITE OUTPUT TO TEST.DAT AND UPLOAD TO CLP ======================
#==============================================================================
# file = open("TEST.dat","w")
# for clas in querry_classes:
#     if clas > 0:
#         file.write("+1\n")
#     else:
#         file.write("-1\n")
# file.close()
#==============================================================================

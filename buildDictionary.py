# -*- coding: utf-8 -*-
import pandas as pd
from collections import defaultdict
import pickle
import time

start_time = time.time()

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

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
save_obj(index, "dictionary")

read = load_obj("dictionary")
print read
end = time.time()

time = end - start_time
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
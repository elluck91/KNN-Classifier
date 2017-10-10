# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_csv(
    filepath_or_buffer='backup data/test.dat', 
    header=None, 
    sep='\n')

# separate names from classes
vals = df.iloc[:,:].values
clas1 = [int(n[0]) for n in vals]
print clas1

f = pd.read_csv(
    filepath_or_buffer='test.dat', 
    header=None, 
    sep='\n')

# separate names from classes
values = f.iloc[:,:].values
clas2 = [int(n[0]) for n in values]

sum = 0.0
for i in range(0, 25000):
    print str(clas1[i]) + " == " + str(clas2[i])
    if clas1[i] == clas2[i]:
        sum += 1

print "This many outputs are the same: " + str(sum/len(clas1))

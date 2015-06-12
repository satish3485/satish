"""Selection sort algorithm"""

import sys



f = open('data.txt')
data = [int(x) for x in f.readline().split()]
f.close()
ls = data
        
for i in range(0, len(ls) - 1):
    pos = i
    for j in range(i+1, len(ls)):
        if ls[j] < ls[pos]:
            pos = j
    ls[pos], ls[i] = ls[i], ls[pos]


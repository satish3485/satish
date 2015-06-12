#!/usr/bin/python
import sys

dat = []
f = int(input())
while f != '':
       dat.append(f)
       f = input()

for i in range(0, len(dat) - 1):
        pos = i
        for j in range(i+1, len(dat)):
            if int(dat[j]) < int(dat[pos]):
                pos = j
        dat[pos], dat[i] = dat[i], dat[pos]
print(dat)

#!/usr/bin/python
import sys
data = []

def better_algo_Y(filename):
       f = open(filename,'r')
       for line in f.readline().strip().split():
              data.append(int(line))
       f.close()
       return msort2(data)
def msort2(x):
    result = []
    if len(x) < 2:
       return x        
    mid = int(len(x)/2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    if len(result)==len(data):
           return algo_Y(result)
    return result

def algo_Y(x):
       m = []
       for i in range(len(x)):
              j = i + 1
              if j < len(x):

                     if x[i] < x[j]:
                            R = [x[i], x[j]]
                            s = x[j] - x[i]
                     else:
                            R= [x[j], x[i]]
                            s = x[i] - x[j]
                     k=0
                     while k < len(x):
                            if x[k] == R[0] -(R[1] - R[0]):
                                   R.insert(0,x[k])
                                   k=0
                            elif x[k] == R [-1] + (R [- 1] - R [- 2]) :
                                   R.append(x[k])
                                   k=0
                            else:
                                   k += 1
                     if len(R) > len(m):
                            m = R
              
       return m

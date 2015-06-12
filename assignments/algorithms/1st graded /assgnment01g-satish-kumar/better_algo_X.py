#!/usr/bin/python
import sys
data = []
def better_algo_X(filename):
       f = open(filename,'r')
       for line in f.readline().strip().split():
              data.append(line)
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
            if str(y[0]) > str(z[0]):
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    if len(result)==len(data):
           return algo1(result)
    return result

lis = []
extra = []
def algo1(a):
       i=0
       
       while i < len(a):
              if i < len(a)-1:
                     if a[i] == a[i+1]:
                            lis.append(a[i])
                            i = i+2
                     else:
                            extra.append(a[i])
                            
                            i+=1
              else:
                     extra.append(a[i])
                     i+=1
       
       
       if len(extra)>2:
              return 'False'
       else:
              return 'True'

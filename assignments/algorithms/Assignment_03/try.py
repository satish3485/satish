#!/usr/bin/python
import sys

def hiccup_Sort(a):
       
       m = 0
       
       for r in range(len(a)-2):
              if r%2 == 0:
                     if a[m] > a[r+2]:
                            a[m],a[r+2] = a[r+2],a[m]
                            m = r+2
       n = 1
       
       for r in range(len(a)-2):
              if r%2 == 1:
                     if a[n] < a[r+2]:
                            a[n],a[r+2] = a[r+2],a[n]
                            n = r+2             


##       i = 0
##       s = 0
##       while i < len(a)-2:
##              if a[s] > a[i+2]:
##                    
##                    a[s],a[i+2] = a[i+2],a[s]
##                    s = i+2
##              i = i+2
##
##


                    
print('please write input in list')
a=[]
for line in sys.stdin.readline().strip().split():
    try:
        a.append(int(line))
        
    except ValueError:
        pass 


print(hiccup_Sort(a))

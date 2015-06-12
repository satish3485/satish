#!/usr/bin/python
import sys

def hiccup_Sort(a):
       
       for r in range(len(a)):
              s = r
              while s < len(a):
                     if r % 2 == 1:
                            if a[r] < a[s]:
                                   a[r],a[s] = a[s],a[r]
                            s = s+1

                     else:
                            if a[r] > a[s]:
                                   a[r],a[s] = a[s],a[r]
                            s = s+1                           

       return a
print('please write input in list')
a=[]
for line in sys.stdin.readline().strip().split():
    try:
        a.append(int(line))
        
    except ValueError:
        pass 


print(hiccup_Sort(a))

#!/usr/bin/python
import sys
data = []
s = []
def check_distance(x,key):
    result = []
    if len(x) < 2:
       return x        
    mid = int(len(x)//2)
    y = check_distance(x[:mid],key)
    z = check_distance(x[mid:],key)
    while (len(y)> 0) and (len(z) > 0):
           if y[0] > z[0]:
                  if (y[0]-z[0]) < key:
                         s.append(y[0])
                  result.append(z[0])
                  z.pop(0)
           else:
                if (z[0]-y[0]) < key:
                       s.append(z[0])
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    if len(result)==len(data):
       if len(s) > 0:
              return False
              
       else:
              return True
              
    return result

print('please write input in list')
x=[]
for line in sys.stdin.readline().strip().split():
    try:
        x.append(int(line))
        data.append(int(line))
    except ValueError:
        pass 
key = input('please enter key:')

print(check_distance(x,int(key)))

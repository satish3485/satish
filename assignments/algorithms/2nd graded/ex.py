#!/usr/bin/python
import sys
data=[]
def msort2(x,key):
    result = []

    if len(x) < 2:
       return x       
    mid = int(len(x)//2)
    y = msort2(x[:mid],key)
    z = msort2(x[mid:],key)
    while (len(y)> 0) and (len(z) > 0):
           if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
           else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    print(result)
    if len(result)==len(data):
       s = 0
       for i in range(len(result)-1):
              if (result[i+1] - result[i]) < key :
                     s = s + 1
       if s > 0:
              print(False)
              return
       else:
              print(True)
              return
    return result

s=[]
print('x list')
for line in sys.stdin.readline().strip().split():
    s.append(int(line))
    data.append(int(line))
a = []
print('y list')
for line in sys.stdin.readline().strip().split():
    a.append(int(line))
    data.append(int(line))

key = input('please enter key:')
while not key.isnumeric():
       key = input('please enter a number key:')
msort2(x,int(key))

#!/usr/bin/python
import sys
data = []
s = []
def msort2(x,a,key):
    result = []
    if len(x) < 2:
       return x        
    mid = int(len(x)//2)
    r = int(len(a)//2)
    y = msort2(x[:mid],a[:r],key)
    z = msort2(x[mid:],a[r:],key)
    print(y,z)
    while (len(y)> 0) and (len(z) > 0):
           if ((y[0]- z[0])**2+(z[1]-y[1])**2) < key**2:
                  s.append(z[0])
                  result.append(z[0])
                  z.pop(0)
                  z.pop(0)
           else:
                result.append(y)
                y.pop(0)
                y.pop(0)
    return result
x=[]
print('x list')
for line in sys.stdin.readline().strip().split():
    x.append(int(line))
    data.append(int(line))
a = []
print('y list')
for line1 in sys.stdin.readline().strip().split():
    a.append(int(line1))
    data.append(int(line1))
key = input('please enter key:')
while not key.isnumeric():
       key = input('please enter a number key:')

print(msort2(x,a,int(key)))

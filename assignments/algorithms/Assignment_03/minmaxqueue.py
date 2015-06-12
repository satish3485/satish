#!/usr/bin/python
import sys
a = []
b = []
m = []

def maxheap():
       if len(a) == 2:
              
              if a[0] < a[1]:
                     a[0],a[1] = a[1],a[0]
                     
       else:
              i = len(a)-1
              while i > 0:
                     if a[i] > a[(i//2)]:
                            a[i],a[(i//2)] = a[(i//2)],a[i]
                     i = (i//2)

def maxheap2():
       if len(a) == 2:
              
              if a[0] < a[1]:
                     a[0],a[1] = a[1],a[0]
                     
       else:
              i = len(a)-2
              while i > 0:
                     if a[i] > a[(i//2)]:
                            a[i],a[(i//2)] = a[(i//2)],a[i]
                     i = (i//2)
                     


def minheap():
       if len(b) == 2:
              
              if b[0] > b[1]:
                     b[0],b[1] = b[1],b[0]
                     
       else:
              i = len(b)-1
              while i > 0:
                     if b[i] < b[(i//2)]:
                            b[i],b[(i//2)] = b[(i//2)],b[i]
                     i = (i//2)

def minheap2():
       if len(b) == 2:
              
              if b[0] > b[1]:
                     b[0],b[1] = b[1],b[0]
                     
       else:
              i = len(b)-2
              while i > 0:
                     if b[i] < b[(i//2)]:
                            b[i],b[(i//2)] = b[(i//2)],b[i]
                     i = (i//2)
                     



def getmin2():
       
       print('getmin', b[0])
       b[-1],b[0] = b[0],b[-1]
       b.pop()
       minheap()
       minheap2()
       m.pop()

def getmin():
       if m == []:
              print('list is empty')
              global a
              a = []
              global b
              b = []
       else:
              getmin2()      
      
def getmax2():
    print('getmax', a[0])
    a[-1],a[0] = a[0],a[-1]
    a.pop()
    maxheap()
    maxheap2()
    m.pop()

def getmax():
       if m == []:
              print('list is empty')
              global a
              a = []
              global b
              b = []
       else:
              getmax2()
                     
def add(x):
       m.append(int(x))
       a.append(int(x))
       b.append(int(x))
       maxheap()
       minheap()
       print('added ', x)

#!/usr/bin/python

import sys


def check_duplicate(x):
    if len(x)> 1:

        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]
        if ((check_duplicate(left)) == True) or ((check_duplicate(right)) == True):
            return True

        
        nl = len(left)
        nr = len(right)
        i = 0
        j = 0
        k = 0
        while i < nl and j < nr:
            if str(left[i]) == str(right[j]):
                return True
            elif str(left[i]) <= str(right[j]):
                x[k]=left[i]
                k = k + 1
                i = i + 1
            else:
                x[k]=right[j]
                k = k + 1
                j = j + 1
        while i < nl :
            x[k]=left[i]
            k = k + 1
            i = i + 1
        while j < nr :
            x[k]=right[j]
            k = k + 1
            j = j + 1
            
    return False


x=[]
for line in sys.stdin.readline().strip().split():
    try:
        x.append(int(line))
    except ValueError:
        pass 

print(check_duplicate(x))



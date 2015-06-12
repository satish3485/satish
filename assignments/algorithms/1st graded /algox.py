A = [7,2,3,5,2,3,2,5,7]
def algo(A):
       i=0
       j = (len(A) - 1)
       n = 1
       while i < j:
              s = i + n
              if A[i]==A[j]:
                     i += 1
                     j -= 1
                     
              elif A[i] == A[s]:
                     A[j],A[s] = A[s],A[j]
                     i += 1
                     j -= 1
              elif A[j] == A[s]:
                     A[i],A[s] = A[s],A[i]
                     i += 1
                     j -= 1
              elif s == j:
                     n = 1
                     j -= 1
                     return False
              else:
                     n += 1
                     
       return True

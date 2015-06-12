def algo_Y(A):
       M = []
       for i in range(len(A)):
              for j in range(i):
                     if A[i] < A[j]:
                            R = [A[i], A[j]]
                     else:
                            R= [A[j], A[i]]
                     k=0
                     while k < len(A):
                            if A[k] == R[0] -(R[1] - R[0]):
                                   R.insert(0,A[k])
                                   k=0
                            elif A[k] == R [-1] + (R [- 1] - R [- 2]) :
                                   R.append(A[k])
                                   k=0
                            else:
                                   k += 1
                     if len(R) > len(M):
                            M = R
       return M

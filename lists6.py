A = [1,2,3,2,3,3]

for i in range(1,len(A)):
    if A.count(A[i]) == 1:
        print(A[i], end = ' ')

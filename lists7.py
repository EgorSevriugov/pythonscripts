A = [1,2,3,2,3,3,2]
S = []
for i in range(1,len(A)):
    if A.count(A[i]) > A.count(A[i-1]):
        S = [A[i]]
    elif (A.count(A[i]) == A.count(A[i-1])) and not A[i] in S: 
        S.append(A[i])
print (S)

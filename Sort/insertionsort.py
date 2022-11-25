def insertionsort(A):
    for i in range(1,len(A)):
        for j in range(i,0,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
            else:
                break
    return A

A=[1,2,7,3,5,9,3]
print(insertionsort(A))
def BubbleSort(A):
    for i in range(len(A)-1,1,-1):
        for j in range(1,i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

A=[1,2,7,3,5,9,3]
print(BubbleSort(A))

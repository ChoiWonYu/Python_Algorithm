from random import randrange
import time
def SelectionSort(A):
    for i in range(1,len(A)):
        minIdx=i
        for j in range(i,len(A)):
            if A[j]<A[i]:
                minIdx=j
        A[i],A[minIdx]=A[minIdx],A[i]
    return A
A=[12, 70 ,30, 20 ,55 ,25]
print(SelectionSort(A))
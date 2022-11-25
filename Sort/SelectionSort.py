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

A=[1,2,7,3,5,9,3]


a=[]
for i in range(20000):
    a.append(randrange(100000))
start=time.time()
SelectionSort(A)
end=time.time()

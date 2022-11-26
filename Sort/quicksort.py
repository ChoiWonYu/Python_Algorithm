import time
from random import randrange
a=[]
for i in range(100000):
    a.append(randrange(100000))
def quicksort(A,start,end):
    def partition(A,start,end):
        x=A[end]
        i=start-1
        for j in range(start,end):
            if A[j]<x:
                i+=1
                A[i],A[j]=A[j],A[i]
        A[i+1],A[end]=A[end],A[i+1]
        return i+1
    if start<end:
        q=partition(A,start,end)
        quicksort(A,start,q-1)
        quicksort(A,q+1,end)




def partition(A, start, end):
    x = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1

start=time.time()
quicksort(a,0,len(a)-1)
end=time.time()
sortTime=end-start
print(f'{sortTime:.10f}')
import time
from random import randrange
a=[]
time_sum=0
for i in range(100000):
    a.append(randrange(100000))
def heapsort(A):
    def percolateDown(A,k:int,end:int):
        child=2*k+1
        right=2*k+2
        if child<=end:
            if right<=end and A[child]<A[right]:
                child=right
            if A[k]<A[child]:
                A[k],A[child]=A[child],A[k]
                percolateDown(A,child,end)
    def buildHeapSort(A):
        for i in range((len(A)-2)//2,-1,-1):
            percolateDown(A,i,len(A)-1)
    buildHeapSort(A)
    for last in range(len(A)-1,0,-1):
        A[last],A[0]=A[0],A[last]
        percolateDown(A,0,last-1)
start=time.time()
heapsort(a)
end=time.time()
sortTime=end-start
print(f'{sortTime:.10f}')

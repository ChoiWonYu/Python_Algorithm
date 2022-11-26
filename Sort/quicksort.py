import time
from random import randrange
a=[]
time_sum=0
for i in range(100000):
    a.append(randrange())
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
A=[12, 70 ,30, 20 ,55 ,25]

quicksort(A,0,len(A)-1)
print(A)
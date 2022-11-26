import time
from random import randrange
a=[]
time_sum=0
for i in range(100):
    a.append(randrange(100000))
def BubbleSort(A):
    for i in range(len(A)-1,1,-1):
        for j in range(1,i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
start=time.time()
BubbleSort(a)
end=time.time()
sortTime=end-start
print(f'{sortTime:.10f}')

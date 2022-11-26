import time
from random import randrange
a=[]
time_sum=0
for i in range(10000):
    a.append(randrange(100000))
def BubbleSort(A):
    for i in range(len(A)-1,1,-1):
        for j in range(1,i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

for i in range(100):
    start=time.time()
    BubbleSort(a)
    end=time.time()
    time_sum+=end-start
aver=time_sum/100
print(f'{aver:.10f}')

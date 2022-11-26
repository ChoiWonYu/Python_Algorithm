from insertionsort import insertionsort

import math
import time
from random import randrange
a=[]
time_sum=0
for i in range(100000):
    a.append(randrange())




def bucketsort(arr):
    n=len(arr)
    B=[[]for _ in range(n)]
    for i in range(n):
        B[math.floor(n*arr[i])].append(arr[i])
    arr.clear()
    for i in range(n):
        insertionsort(B[i])
        arr.extend(B[i])


for i in range(100):
    start=time.time()
    bucketsort(a)
    end=time.time()
    time_sum+=end-start
aver=time_sum/100
print(f'{aver:.10f}')
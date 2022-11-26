from insertionsort import insertionsort

import math
import time
from random import random
a=[]
time_sum=0
for i in range(1000):
    a.append(random())




def bucketsort(arr):
    n=len(arr)
    B=[[]for _ in range(n)]
    for i in range(n):
        B[math.floor(n*arr[i])].append(arr[i])
    arr.clear()
    for i in range(n):
        insertionsort(B[i])
        arr.extend(B[i])


start=time.time()
bucketsort(a)
end=time.time()
Time=end-start
print(f'{Time:.10f}')
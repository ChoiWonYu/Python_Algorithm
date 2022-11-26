import time
from random import randrange
a=[]
timeSum=0
for i in range(100):
    a.append(randrange(100000))
def mergesort(arr):
    def sort(low,high):
        if high-low<2:
            return
        mid=(high+low)//2
        sort(low,mid)
        sort(mid,high)
        merge(low,mid,high)
        return arr
    def merge(low,mid,high):
        tmp=[]
        l,h=low,mid
        while l<mid and h<high:
            if arr[l]<arr[h]:
                tmp.append(arr[l])
                l+=1
            else:
                tmp.append(arr[h])
                h+=1
        while l<mid:
            tmp.append(arr[l])
            l+=1
        while h<high:
            tmp.append(arr[h])
            h+=1
        for i in range(low,high):
            arr[i]=tmp[i-low]
    return sort(0,len(arr))
for i in range(100):
    start=time.time()
    mergesort(a)
    end=time.time()
    timeSum=end-start
aver=timeSum/100
print(f'{aver:.10f}')
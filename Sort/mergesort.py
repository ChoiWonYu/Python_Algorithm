import time
from random import randrange
a=[]
time_sum=0
for i in range(100000):
    a.append(randrange())
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
arr=[12, 70, 30, 20, 55 ,25, 40, 50]
print(mergesort(arr))
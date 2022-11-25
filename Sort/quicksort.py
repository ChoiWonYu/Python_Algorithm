def quicksort(A,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and A[left]<=A[pivot]:
            left+=1
        while right>start and A[right]>=A[pivot]:
            right-=1
        if left>right:
            A[pivot], A[right] = A[right], A[pivot]
        else:
            A[right],A[left]=A[left],A[right]
    quicksort(A,start,right-1)
    quicksort(A,right+1,end)

A=[5,6,7,9,0,3,1,6,2,4,8]
quicksort(A,0,len(A)-1)
print(A)

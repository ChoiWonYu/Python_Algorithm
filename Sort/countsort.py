def countsort(A):
    count=[0]*(max(A)+1)
    returnArr=[0]*len(A)
    idx=0
    for i in range(len(A)):
        count[A[i]]+=1
    for i in range(len(count)):
        for j in range(count[i]):
            returnArr[idx]=i
            idx+=1
    return returnArr

A=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
print(countsort(A))


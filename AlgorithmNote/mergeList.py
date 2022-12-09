a=[1,3,5]
b=[2,4,6,8]
aLen=len(a)
bLen=len(b)

i,j=0,0
arr=[]
while i<aLen or j<bLen:
    if (i<aLen and a[i]>=b[j]) or i==aLen:
        arr.append(b[j])
        j+=1
    else:
        arr.append(a[i])
        i+=1

print(arr)
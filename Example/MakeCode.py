import itertools
Len,count=map(int,input().split())
arr=input().split()
arr.sort()
vowels=['a','e','i','o','u']
result=list(itertools.combinations(arr,Len))
for i in range(len(result)):
    count=0
    tar=result[i]
    for j in range(len(tar)):
        if tar[j] in vowels:
            count+=1
    if count>=1 and count<=2:
        print(''.join(tar))

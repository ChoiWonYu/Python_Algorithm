import itertools
Len,count=map(int,input().split())
arr=input().split()
arr.sort()
vowels=['a','e','i','o','u']
result=list(itertools.combinations(arr,Len))
#combination 객체를 바로 for문으로 쓸 수 있음
for i in range(len(result)):
    count=0
    tar=result[i]
    for j in range(len(tar)):
        if tar[j] in vowels:
            count+=1
    if count>=1 and count<=2:
        print(''.join(tar))

for password in itertools.combinations(arr,Len):
    count=0
    for i in password:
        if i in vowels:
            count+=1
    if count>=1 and count <=2:
        print(''.join(password))
total=int(input())
rep=int(input())
sum=0
for i in range(rep):
    price,x=list(map(int,input().split()))
    sum+=price*x
if total==sum:
    print('Yes')
else:
    print('No')
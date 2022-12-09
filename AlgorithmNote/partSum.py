n=5 #데이터 개수
m=5 #부분합
data=[1,2,3,2,5]
count,end=0,0
sum=0
for start in range(0,n):
    while sum<m and end<n:
        sum+=data[end]
        end+=1
    if sum==m:
        count+=1
    sum-=data[start]
print(count)





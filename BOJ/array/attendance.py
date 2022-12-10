count=30
students=[False for _ in range(count+1)]
for i in range(count-2):
    num=int(input())
    students[num]=True
for i in range(1,count+1):
    if students[i]==False:
        print(i)
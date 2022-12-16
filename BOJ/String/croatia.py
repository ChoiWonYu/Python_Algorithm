arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input().strip()
sum=0
for i in arr:
    sum+=s.count(i)
print(len(s)-sum)
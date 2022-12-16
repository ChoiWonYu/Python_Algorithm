arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
"""
sum=0
for i in arr:
    sum+=s.count(i)
print(len(s)-sum)
"""
for i in arr:
    s=s.replace(i,'*')
print(len(s))
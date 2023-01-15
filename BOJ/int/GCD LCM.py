import sys
input=sys.stdin.readline
a,b=map(int,input().split())
min=a;max=b
if a>b:min=b;max=a
gcd=1
lcm=[]
for i in range(1,min+1):
    if max%i==0 and min%i==0:gcd=i
    if (max*i)%min==0:lcm.append(max*i)
print(gcd)
print(lcm[0])

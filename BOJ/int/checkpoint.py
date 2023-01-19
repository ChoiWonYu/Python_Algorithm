import sys
input=sys.stdin.readline
count=int(input())
l=sorted(int(input()) for _ in range(count))
newL=[]
for i in range(len(l)-1):
    newL.append(l[i+1]-l[i])
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

GCD = newL[0]
for idx in range(1, len(newL)):
    GCD = gcd(GCD, newL[idx])
result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))
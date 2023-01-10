import sys
input=sys.stdin.readline
s=list(map(str,input().strip()))
result=set()
for i in range(len(s)):
    result.add(s[i])
    for j in range(i):
        result.add(''.join(s[j:i+1]))
print(len(result))

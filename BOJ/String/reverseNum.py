"""
n1,n2=input().split()
f=int(''.join(list(reversed(list(map(str,n1))))))
s=int(''.join(list(reversed(list(map(str,n2))))))
if f>s:print(f)
else: print(s)
"""
print(max(list(map(int,input()[::-1].split(' ')))))
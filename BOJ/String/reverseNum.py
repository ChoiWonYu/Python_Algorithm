"""
n1,n2=input().split()
f=int(''.join(list(reversed(list(map(str,n1))))))
s=int(''.join(list(reversed(list(map(str,n2))))))
if f>s:print(f)
else: print(s)
"""
print(max(list(map(int,input()[::-1].split(' ')))))

"""
list slicing
a[start:end:step]
start : slicing을 시작할 인덱스
end : slicing을 끝낼 인덱스 (끝은 포함하지 않음)
step ?: 몇개씩 끊어서 가져올지
"""
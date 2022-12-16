import sys
n=int(input())
for _ in range(n):
    r,s=sys.stdin.readline().rstrip().split()
    for i in s:
        print(i*int(r),end="")
    print()




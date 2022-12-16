"""
import sys
print(len(sys.stdin.readline().strip().split()))
"""
a=input().strip()
if len(a)>=1:
    print(a.count(" ")+1)
else:
    print(0)
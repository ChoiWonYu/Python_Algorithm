# n=int(input())
# sum = 0
# for _ in range(n):
#     s=input()
#     for i in set(s):
#         if s.count(i) > 1:
#             sc = ('*' + s + '*').split(i)
#             while ''in sc:
#                 sc.remove('')
#             if len(sc) > 2:
#                 sum-=1
#                 break
#     sum += 1
# print(sum)

N = int(input())
res = N
for i in range(N):
    s = input()
    d = set(s)
    if sum(map(lambda x: s.rfind(x) - s.find(x)+1, d)) != len(s):
        res -= 1
print(res)

"""
lambda 매개변수:표현식
ex) (lambda x,y:x+y)(10,20)
    map(lambda x:x**2,range(4))
"""
n=int(input())
sum = 0
for _ in range(n):
    s=input()
    for i in set(s):
        if s.count(i) > 1:
            sc = ('*' + s + '*').split(i)
            while ''in sc:
                sc.remove('')
            if len(sc) > 2:
                sum-=1
                break
    sum += 1
print(sum)
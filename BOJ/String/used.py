#65~90
s=input().upper()
b=[]
for i in range(65,91):
    b.append(s.count(chr(i)))
if b.count(max(b))>1:print('?')
else:
    print(chr(65+b.index(max(b))))
origin=[1,1,2,2,2,8]
ques=list(map(int,input().split()))
ans=[str(origin[idx]-i) for idx,i in enumerate(ques)]
print(' '.join(ans))



dice=list(map(int,input().split()))
for i in dice:
    if dice.count(i)==2:
        print(1000+i*100)
        exit(0)
    elif dice.count(i)==3:
        print(10000+i*1000)
        exit(0)
print(max(dice)*100)


arr=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
key=list(map(str,input()))
sum=0
for i in key:
    for j in arr:
        if i in j:
            sum+=3+arr.index(j)
            break
print(sum)

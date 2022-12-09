data=[10,20,30,40,50]
prefixSum=[0]
sum=0
for i in range(len(data)):
    sum+=data[i]
    prefixSum.append(sum)

left=3
right=4
print(prefixSum[right]-prefixSum[left-1])

from itertools import permutations,product,combinations_with_replacement,combinations
import heapq
from bisect import bisect_left,bisect_right
from collections import deque,Counter
import math

#sum
result=sum([1,2,3])
print(result)       #6

#min, max
a=[1,2,3,6,7,4]
print(min(a))       #1
print(max(a))       #7

#eval
print(eval("1+2*4+(1+4)"))  #14

#sorted()
print(sorted([1,2,6,3,7,5]))    #[1, 2, 3, 5, 6, 7]
print(sorted([1,2,6,3,7,5],reverse=True))    #[7, 6, 5, 3, 2, 1]

#iter

data=['A','B','C']
print(list(permutations(data,2)))
#[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

print(list(product(data,repeat=2)))
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

print(list(combinations(data,2)))
#[('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(combinations_with_replacement(data,2)))
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


#heap

def heapsort(iter):
    h=[]
    result=[]
    for value in iter:
        #heap으로 push되면서 정렬된다.
        heapq.heappush(h,value)
    for _ in range(len(h)):
        #정렬된 원소들을 빼면서 result에 삽입한다.
        result.append(heapq.heappop(h))
    #정렬된 원소들의 리스트 result를 반환한다.
    return result
result=heapsort([1,3,5,2,6,4,8,9])
print(result)                           #[1, 2, 3, 4, 5, 6, 8, 9]

def Mheapsort(iter):
    h=[]
    result=[]
    for value in iter:
        #heap으로 push되면서 정렬된다.
        heapq.heappush(h,-value)
    for _ in range(len(h)):
        #정렬된 원소들을 빼면서 result에 삽입한다.
        result.append(-heapq.heappop(h))
    #정렬된 원소들의 리스트 result를 반환한다.
    return result
result=Mheapsort([1,3,5,2,6,4,8,9])
print(result)                           #[9, 8, 6, 5, 4, 3, 2, 1]


#bisect

a=[1,2,3,3,5]
x=3

print(bisect_left(a,x))     #2
print(bisect_right(a,x))    #4


#deque

data=deque([1,2,3])
data.appendleft(9)
data.append(5)
print(data)             #deque([9, 1, 2, 3, 5])
print(list(data))       #[9, 1, 2, 3, 5]
data.rotate(2)
print(data)

#Counter

counter=Counter(['red','blue','orange','red','red','blue'])
print(dict(counter))                                            #{'red': 3, 'blue': 2, 'orange': 1}
print(counter['red'])                                           #3


#math

print(math.factorial(6))    #720
print(math.sqrt(8))         #2.8284271247461903
print(math.gcd(21,14))      #7
print(math.pi)              #3.141592653589793
print(math.e)               #2.718281828459045
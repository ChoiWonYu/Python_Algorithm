import math
import sys
#실수
a=1e9       #10억의 지수 표현 방식
print(a)    #1000000000.0

b=0.9912314
print(round(b))       #0.991
print(math.ceil(b))     #1
print(math.floor(b))    #0

#리스트

#크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
N=10
c=[0]*N
print(c)    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

d=[1,2,3,4,5,6,7]
print(d[4:-1])      #[5, 6]

#0부터 19까지의 수 중에 홀수만 포함하는 리스트
e=[i for i in range(20) if i%2==1]
print(e)                            #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#1부터 9까지 수의 제곱 값을 포함하는 리스트
f=[i*i for i in range(1,10)]
print(f)                            #[1, 4, 9, 16, 25, 36, 49, 64, 81]

#N X M 크기의 2차원 리스트 초기화
n=3
m=4
arr=[[0]*m for _ in range(n)]
print(arr)                          #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

g=[1,2,3,3,4,4,4,5]
remove_set=[3,4]

result=[i for i in g if i not in remove_set]
print(result)                                   #[1, 2, 5]


#집합

data=set([1,1,2,3,4,5,5])
print(data)                 #{1, 2, 3, 4, 5}

data={1,2,2,3,4,4,5}
print(data)                 #{1, 2, 3, 4, 5}



#함수

print((lambda a,b:a+b)(3,7))    #10


#입출력

# data=list(map(int,input().split()))
# print(input().split())

data=sys.stdin.readline().rstrip()
print(data)

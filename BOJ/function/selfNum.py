data=10000
def makeSelfNum(n:int)->int:
    n+=sum(map(int,str(n)))
    return n
print(makeSelfNum(31))
#
# arr=[True for _ in range(data+1)]
# for i in range(1,data+1):
#     if makeSelfNum(i)<=data:
#         arr[makeSelfNum(i)] = False
# for i in range(1,data+1):
#     if arr[i]==True:
#         print(i)


"""
map 함수를 통해 각 자리 수를 더할 수 있음.
sum(map(int,str(n)))
->str(n)이 숫자를 문자열로 바꿔주고,
map 함수가 map객체로 변환하면서 각 원소를 int로 바꿔준다.
->sum으로 모두 합한다.
"""
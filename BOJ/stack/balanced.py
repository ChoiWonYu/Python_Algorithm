import sys
input=sys.stdin.readline

def isBalanced(str):
    s=[]

    for i in str:
        if i=='(' or i=='[':
            s.append(i)
        elif i==')':
            if len(s)==0:
                return False
            else:
                if s.pop()!='(':
                    return False
        elif i==']':
            if len(s)==0:
                return False
            else:
                if s.pop()!='[':
                    return False
    if len(s)==0:
        return True
    return False

while 1:
    n=input().rstrip()
    if n=='.':
        break
    else:
        if isBalanced(n.strip()):
            print('yes')
        else:
            print('no')
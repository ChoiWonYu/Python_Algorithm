def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result

def bino_coef(n,k):
    return factorial(n)//factorial(n-k)//factorial(k)
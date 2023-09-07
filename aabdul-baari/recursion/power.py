def power(m,n):
    if n == 0:
        return 1
    if n==1:
        return m
    return m*power(m,n-1)

def fast_pow(m,n):
    if n==0:
        return 1
    if n%2 == 0:
        return fast_pow(m*m,n//2)
    return m*fast_pow(m*m,(n-1)//2)



print(fast_pow(2,100))

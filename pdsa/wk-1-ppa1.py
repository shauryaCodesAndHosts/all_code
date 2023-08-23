import math 
def isPrime(n):
    if n == 1 or n==0 or n==2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def lastPrime(n,m):
    for i in range(n,m):
        if isPrime(i):
            return i
    return 0

def Twin_Primes(n,m):
    lastprime=lastPrime(n,m)
    twin=[]
    for i in range(n,m):
        if isPrime(i):
            if (lastprime-i)==(-2):
                twin.append((lastprime,i))
            lastprime=i; 
    return twin
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
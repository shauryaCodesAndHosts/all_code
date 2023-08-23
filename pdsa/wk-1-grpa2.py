import math
def isPrime(n):
    if n == 1 or n==0 or n==2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def Goldbach(n):
    primes=[]
    for i in range(0,n):
        if isPrime(i):
            primes.append(i)
    #print(primes)
    l=[]
    for i in range(0,len(primes)):
        for j in range(i,len(primes)):
            #print(primes[i], primes[j])
            if (primes[i]+primes[j]) == n:
                l.append((primes[i],primes[j]))
    return l 

n=int(input())
print(sorted(Goldbach(n)))

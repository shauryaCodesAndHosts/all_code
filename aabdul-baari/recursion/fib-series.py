def memFib(n,arr):
    if n== 0:
        arr[n] = 0
        return 0
    elif n==1:
        arr[n] = 1
        return 1
    elif arr[n] != -1:
        return arr[n]
    else:
        if arr[n-2] == -1:
            arr[n-2] = memFib(n-2,arr)
        if arr[n-1] == -1:
            arr[n-1] = memFib(n-1,arr)
        return arr[n-1]+arr[n-2]
        



def fib(n):
    if n==0:
        return 0
    if n==1 :
        return 1
    else:
        #print(n,end="  ")
        return fib(n-1)+fib(n-2)
    
print(memFib(7,[-1,-1,-1,-1,-1,-1,-1,-1]))
def minmax(a,b):
    for i in range(0,len(a)):
        if a[i]<b[i]:
            t=a[i]
            a[i]=b[i]
            b[i]=t
    return max(a)*max(b)


print(minmax([1,2,6,5,1,2],[3,4,3,2,2,5]))
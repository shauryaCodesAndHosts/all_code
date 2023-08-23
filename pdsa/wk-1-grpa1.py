import math
import sys

def find_Min_Difference(L,P):
    minm=sys.maxsize
    min_syntax=0
    L.sort()
    print(L)
    for i in range(0,len(L)-P+1):
        end=i + P - 1 
        diff=abs(L[end]-L[i])
        print(diff)
        if diff < minm:
            min_syntax = i
            minm=diff
    return minm


L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
def soln(ls,n):
    min_index=0
    for i in range(0,n):
        for i in range(0,len(ls)):
            if ls[i]<ls[min_index]:
                min_index=i
                print(ls[min_index])
        ls[min_index]=ls[min_index]+1
    prod=1
    for i in ls:
        prod=prod*i
    print(ls)
    print(prod)



def soln2(ls,n):
    dic={}
    for x in ls:
        dic[x]=0
        


soln([2,0,4,3],4)
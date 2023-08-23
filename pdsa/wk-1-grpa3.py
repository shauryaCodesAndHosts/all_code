def odd_one(l):
    type_str=''
    for i in range(0,len(l)):
        if type(l[i]) == type(l[i+1]):
            type_str=type(l[i])
            break
    #print(type_str)
    for i in range(0,len(l)):
        if type(l[i]) != type_str :
            type_str = type(l[i])
            break
    return type_str.__name__
    



print(odd_one(eval(input().strip())))
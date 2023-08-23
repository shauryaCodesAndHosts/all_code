def DishPrepareOrder(nums):
    l=[]
    uni_num=list(set(nums))
    c_dict={}
    for i in range(0,len(uni_num)):
        c=0
        for j in range(0,len(nums)):
            if nums[j] == uni_num[i]:
                c=c+1
        c_dict[uni_num[i]]=c
    #max_count=0
    #max_val=0
    #print(c_dict)
    #print(uni_num)
    #l_count=c_dict.items()
    l=sorted(c_dict.items(), key=lambda x: x[1],reverse=True)
    #print(l)
    ls=[]
    for i in range(0,len(l)):
        ls.append(l[i][0])
    return ls
    '''for i in range(0,len(l_count)):
        for j in range(0,len(l_count)):
'''


    '''    for i in range(0,len(uni_num)):
        max_count=c_dict[uni_num[i]]
        max_val=uni_num[i]
        for j in range(i,len(uni_num)):
            if c_dict[uni_num[j]]>max_count:
                max_count=c_dict[uni_num[j]]
                max_val=uni_num[j]
            
        print(max_val)
        del c_dict[max_val]
        uni_num.remove(max_val)
        l.append(max_val)
    return l        '''

nums = eval(input())
print(DishPrepareOrder(nums))





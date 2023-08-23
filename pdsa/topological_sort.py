class Queue:
    def __init__(self) -> None:
        self.queue =[]
    
    def addq(self,v):
        self.queue.append(v)

    def isEmpty(self):
        return (self.queue == [] )

    def delq(self):
        v=None
        if not self.isEmpty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v


def toposort(Amat):
    rows = len(Amat)
    cols = len(Amat[0])
    indegree = {}
    toposortlist = []

    for c in range(cols):
        indegree[c]= 0
        for r in range(rows):
            if Amat[r][c] == 1:
                indegree[c]+=1
    #print(indegree) 
    j=None
    for r in range(rows):
        for k in indegree.keys():
            if indegree[k] == 0:
                indegree[k]-=1
                toposortlist.append(k)
                j=k
                break
        #indegree[j]-=1
        print(indegree)
        print(toposortlist)
        for col in range(cols):
            if Amat[j][col] == 1:
                indegree[col] = indegree[col] - 1
        print(indegree)
        print(toposortlist)
    print(toposortlist)
    print(indegree)

m=[
    [0,0,1,1,1,0,0,0],
    [0,0,1,0,0,0,0,1],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0]
]
#toposort(m)



def toposort_adjList(Alist):
    indegree = {}
    toposortList=[]
    for k in Alist.keys():
        indegree[k] = 0
    for k in Alist.keys():
        for l in Alist[k]:
            indegree[l] = indegree[l]+1
    
    zeroq = Queue()
    for k in Alist.keys():
        if indegree[k] == 0 :
            indegree[k]-=1
            zeroq.addq(k)

    while(not zeroq.isEmpty()):
        j= zeroq.delq()
        toposortList.append(j)
        indegree[j]= indegree[j]-1
        for k in Alist[j]:
            indegree[k]-=1
            if indegree[k] == 0:
                zeroq.addq(k)

    print(toposortList)


d={
    0:[2,3,4],
    1:[2,7],
    2:[5],
    3:[5,7],
    4:[7],
    5:[6],
    6:[7],
    7:[]
}

toposort_adjList(d)